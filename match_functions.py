import numpy as np
import cv2
from skimage.transform import rescale


# from matplotlib import pyplot as plt


def imagerescale(image, rescale_factor):
    # rescale with Nearest-neighbor  Order 0: Nearest-neighbor
    image_re = rescale(image, (1, rescale_factor), order=0, mode='reflect')
    return image_re


def get_interest_points(image, feature_width, k, t, r):
    """ Returns a set of interest points for the input image
    Args:
        image - can be grayscale or color, your choice.
        feature_width - in pixels, is the local feature width. It might be
            useful in this function in order to (a) suppress boundary interest
            points (where a feature wouldn't fit entirely in the image)
            or (b) scale the image filters being used. Or you can ignore it.
    Returns:
        x and y: nx1 vectors of x and y coordinates of interest points.
        confidence: an nx1 vector indicating the strength of the interest
            point. You might use this later or not.
        scale and orientation: are nx1 vectors indicating the scale and
            orientation of each interest point. These are OPTIONAL. By default you
            do not need to make scale and orientation invariant local features.
    """
    h, w = image.shape[:2]
    # TODO Write harrisdetector function based on the illustration in specification.
    # Return corner points x-coordinates in result[0] and y-coordinates in result[1]
    image = image.astype(float)

    #    k = 8       # change to your value k = 8
    #    t = 0.10     # change to your value    t = 0.1

    image = np.pad(image, (k, k), 'edge')
    # Laplace gradient kernal
    x_dev_kernal = np.array([[0, 0, 0], [-1, 0, 1], [0, 0, 0]])
    y_dev_kernal = np.array([[0, -1, 0], [0, 0, 0], [0, 1, 0]])
    # Laplace gradient
    x_dev = cv2.filter2D(image, -1, x_dev_kernal)
    y_dev = cv2.filter2D(image, -1, y_dev_kernal)

    Ixx = x_dev ** 2
    Iyy = y_dev ** 2
    IxIy = x_dev * y_dev

    eigen_values_map = np.zeros_like(image)
    for i_x in range(k, h + k):
        for i_y in range(k, w + k):
            A11 = Ixx[i_x - k:i_x + k + 1, i_y - k:i_y + k + 1]
            A21 = IxIy[i_x - k:i_x + k + 1, i_y - k:i_y + k + 1]
            A22 = Iyy[i_x - k:i_x + k + 1, i_y - k:i_y + k + 1]

            A11 = A11.sum()
            A21 = A21.sum()
            A22 = A22.sum()

            A = np.array([[A11, A21], [A21, A22]], dtype=np.float32)
            ret, eigenvalues, eigen_vector = cv2.eigen(A, False)
            if abs(eigenvalues[0]) > t and abs(eigenvalues[1]) > t:
                eigen_values_map[i_x, i_y] = eigenvalues[0] * eigenvalues[1]

    eigen_values_map = eigen_values_map[k:k + h, k:k + w]
    # local max
    # r = 5
    for i in range(h - r):
        for j in range(w - r):
            window = eigen_values_map[i:i + r, j:j + r]
            if window.sum() == 0:
                continue
            else:
                local_max = np.max(window)
            # zero all but the localMax in the window
            max_x, max_y = (window == local_max).nonzero()
            window[:] = 0
            window[max_x, max_y] = local_max
            eigen_values_map[i:i + r, j:j + r] = window

    x, y = (eigen_values_map > 0).nonzero()
    x = x.reshape(len(x), 1)
    y = y.reshape(len(y), 1)

    return y, x


def get_features(image, x, y, feature_width, GB_k):
    """ Returns a set of feature descriptors for a given set of interest points.
    Args:
        image - can be grayscale or color, your choice.
        x and y: nx1 vectors of x and y coordinates of interest points.
            The local features should be centered at x and y.
        feature_width - in pixels, is the local feature width. You can assume
            that feature_width will be a multiple of 4 (i.e. every cell of your
            local SIFT-like feature will have an integer width and height).
        If you want to detect and describe features at multiple scales or
            particular orientations you can add other input arguments.
    Returns:
        features: the array of computed features. It should have the
            following size: [length(x) x feature dimensionality] (e.g. 128 for
            standard SIFT)
    """

    # Placeholder that you can delete. Empty features.
    features = np.zeros((x.shape[0], 128))
    x_ = x.astype(int)
    y_ = y.astype(int)
    y = np.squeeze(x_)
    x = np.squeeze(y_)
    h, w = image.shape[:2]
    # pad to avoid 0
    offset = feature_width // 2
    image = np.pad(image, (offset, offset), 'edge')
    x += offset
    y += offset

    # step 1 Gaussian blur whole image
    # GB_k = 7
    blur_image = cv2.GaussianBlur(image, (GB_k, GB_k), sigmaX=0)  # kernal size is changable, 19 is best 69.8%

    # step 2 gradients
    x_kernal = np.array([[-1, 1]])
    Gx = cv2.filter2D(blur_image, -1, x_kernal)
    Gy = cv2.filter2D(blur_image, -1, np.transpose(x_kernal))

    # step 3 magnitude and orientation
    mag = np.sqrt(Gx ** 2 + Gy ** 2)
    orient = np.arctan2(Gy, Gx)
    orient[orient < 0] += np.pi * 2

    # step 4 further weighted by Gaussian
    cell_length = feature_width / 4
    Gau_kernel = cv2.getGaussianKernel(feature_width, feature_width / 2)

    for i in range(x.shape[0]):
        window = mag[int(x[i] - feature_width / 2):int(x[i] + feature_width / 2),
                 int(y[i] - feature_width / 2):int(y[i] + feature_width / 2)]
        window = cv2.sepFilter2D(window, -1, Gau_kernel, np.transpose(Gau_kernel))
        window_orient = orient[int(x[i] - feature_width / 2):int(x[i] + feature_width / 2),
                        int(y[i] - feature_width / 2):int(y[i] + feature_width / 2)]
        for i_x in range(4):
            for i_y in range(4):
                bin = np.zeros(8)
                cell = window[int(i_x * cell_length):int((i_x + 1) * cell_length),
                       int(i_y * cell_length):int((i_y + 1) * cell_length)]
                cell_orient = window_orient[int(i_x * cell_length):int((i_x + 1) * cell_length),
                              int(i_y * cell_length):int((i_y + 1) * cell_length)]
                for angle in range(bin.shape[0]):
                    bin[angle] += np.sum(
                        cell[np.all([cell_orient >= (angle * np.pi / 4), cell_orient < ((angle + 1) * np.pi / 4)], 0)])
                features[i, (i_x * 4 + i_y) * 8:(i_x * 4 + i_y) * 8 + 8] = bin
        # step 6 normalization
        features[i, :] /= np.sqrt(np.sum(features[i, :] ** 2))

    return features


def match_features(features1, features2, threshold=0.0):
    """
    Args:
        features1 and features2: the n x d(feature dim) feature dimensionality features
            from the two images.
        threshold: a threshold value to decide what is a good match. This value
            needs to be tuned.
        If you want to include geometric verification in this stage, you can add
            the x and y locations of the features as additional inputs.
    Returns:
        matches: a k x 2 matrix, where k is the number of matches. The first
            column is an index in features1, the second column is an index
            in features2.
        Confidences: a k x 1 matrix with a real valued confidence for every
            match.
        matches' and 'confidences' can be empty, e.g. 0x2 and 0x1.
    """
    # Placeholder that you can delete. Random matches and confidences
    num_features = max(features1.shape[0], features2.shape[0])
    matched = np.zeros((num_features, 2))
    confidence = np.zeros((num_features, 1))

    for i in range(features1.shape[0]):
        dist = np.sqrt(np.sum((features1[i] - features2) ** 2, axis=1))  # (n2,k)->n2
        smallest = np.min(dist)
        second_smallest = np.partition(dist, 1)[1]
        ratio = smallest / second_smallest
        confidence[i] = 1 / ratio
        matched[i, 0] = i
        matched[i, 1] = np.argmin(dist)

    # Sort the matches so that the most confident onces are at the top of the
    # list. You should probably not delete this, so that the evaluation
    # functions can be run on the top matches easily.
    order = np.argsort(confidence, axis=0)[::-1, 0]
    confidence = confidence[order, :]
    matched = matched[order, :]

    # delete the ones not so confident
    index_x, index_y = (confidence > threshold).nonzero()
    confidence = confidence[index_x, index_y]
    matched = matched[index_x, :]

    return matched, confidence


def image_match(proj_range1, proj_range2, feature_width):
    max_dist = 30
    k = 8
    t = 0.2
    r = 3
    GB_k = 7
    x1, y1 = get_interest_points(proj_range1, feature_width, k, t, r)
    x2, y2 = get_interest_points(proj_range2, feature_width, k, t, r)

    #    np.savez('var',x1,y1,x2,y2)
    image1_features = get_features(proj_range1, x1, y1, feature_width, GB_k)
    image2_features = get_features(proj_range2, x2, y2, feature_width, GB_k)

    # 4) Match features. Szeliski 4.1.3
    ##
    matches1, confidences1 = match_features(image1_features, image2_features)

    # 5) Visualization

    num_pts = matches1.shape[0]  # default 150
    x1_m = x1[matches1[:num_pts, 0].astype(np.int32)]
    y1_m = y1[matches1[:num_pts, 0].astype(np.int32)]
    x2_m = x2[matches1[:num_pts, 1].astype(np.int32)]
    y2_m = y2[matches1[:num_pts, 1].astype(np.int32)]

    ##################remove mismatch
    # max_dist = 30               ###default 50
    l2dist = np.sqrt((x1_m - x2_m) ** 2 + (y1_m - y2_m) ** 2)
    l2dist[l2dist > max_dist] = -1

    x1_mm = x1_m[~(l2dist == -1).all(axis=1), :]
    x2_mm = x2_m[~(l2dist == -1).all(axis=1), :]
    y1_mm = y1_m[~(l2dist == -1).all(axis=1), :]
    y2_mm = y2_m[~(l2dist == -1).all(axis=1), :]

    num_pts_to_visualize = 5000
    x1_mm = x1_mm[:num_pts_to_visualize, 0]
    x2_mm = x2_mm[:num_pts_to_visualize, 0]
    y1_mm = y1_mm[:num_pts_to_visualize, 0]
    y2_mm = y2_mm[:num_pts_to_visualize, 0]

    ######################
    return x1_mm, y1_mm, x2_mm, y2_mm

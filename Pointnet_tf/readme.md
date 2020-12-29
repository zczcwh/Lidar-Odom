Comparison of different 3D single-view single-person HPE approaches on the Human3.6M dataset. The best two scores are marked in red and blue, respectively. Here in model-free approaches, “Direct” indicates the method directly estimating 3D pose without 2D pose representation. “Lifting” indicates the method lifting the 2D pose representation to the 3D space (i.e., 3D pose). “Temporal” means the method using temporal information.

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">Model free methods</th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">Protocol 1 MPJPE</th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">Protocol 2 PMPJPE</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">Approaches</td>
    <td class="tg-0pky">Year</td>
    <td class="tg-0pky">Methods</td>
    <td class="tg-0pky">Dir. </td>
    <td class="tg-0pky">Disc. </td>
    <td class="tg-0pky">Eat. </td>
    <td class="tg-0pky">Greet</td>
    <td class="tg-0pky"> Phone </td>
    <td class="tg-0pky">Photo </td>
    <td class="tg-0pky">Pose </td>
    <td class="tg-0pky">Purch.</td>
    <td class="tg-0pky"> Sit </td>
    <td class="tg-0pky">SitD. </td>
    <td class="tg-0pky">Somke </td>
    <td class="tg-0pky">Wait</td>
    <td class="tg-0pky"> WalkD. </td>
    <td class="tg-0pky">Walk</td>
    <td class="tg-0pky"> WalkT.</td>
    <td class="tg-0pky">Average</td>
    <td class="tg-0pky">Average</td>
  </tr>
  <tr>
    <td class="tg-0pky">Direct</td>
    <td class="tg-0pky">2017</td>
    <td class="tg-0pky">111</td>
    <td class="tg-0pky">67.4</td>
    <td class="tg-0pky">71.9</td>
    <td class="tg-0pky">66.7</td>
    <td class="tg-0pky">69.1</td>
    <td class="tg-0pky">72.0</td>
    <td class="tg-0pky">77.0</td>
    <td class="tg-0pky">65.0</td>
    <td class="tg-0pky">68.3</td>
    <td class="tg-0pky">83.7</td>
    <td class="tg-0pky">96.5</td>
    <td class="tg-0pky">71.7</td>
    <td class="tg-0pky">65.8</td>
    <td class="tg-0pky">74.9</td>
    <td class="tg-0pky">59.1</td>
    <td class="tg-0pky">63.2</td>
    <td class="tg-0pky">71.9</td>
    <td class="tg-0pky">51.9</td>
  </tr>
  <tr>
    <td class="tg-0pky">Direct</td>
    <td class="tg-0pky">2018</td>
    <td class="tg-0pky">112</td>
    <td class="tg-0pky">48.5</td>
    <td class="tg-0pky">54.4</td>
    <td class="tg-0pky">54.4</td>
    <td class="tg-0pky">52.0</td>
    <td class="tg-0pky">59.4</td>
    <td class="tg-0pky">65.3</td>
    <td class="tg-0pky">49.9</td>
    <td class="tg-0pky">52.9</td>
    <td class="tg-0pky">65.8</td>
    <td class="tg-0pky">71.1</td>
    <td class="tg-0pky">56.6</td>
    <td class="tg-0pky">52.9</td>
    <td class="tg-0pky">60.9</td>
    <td class="tg-0pky">44.7</td>
    <td class="tg-0pky">47.8</td>
    <td class="tg-0pky">56.2</td>
    <td class="tg-0pky">41.8</td>
  </tr>
  <tr>
    <td class="tg-0pky"> lifting</td>
    <td class="tg-0pky">2017</td>
    <td class="tg-0pky">113</td>
    <td class="tg-0pky">51.8</td>
    <td class="tg-0pky">56.2</td>
    <td class="tg-0pky">58.1</td>
    <td class="tg-0pky">59.0</td>
    <td class="tg-0pky">69.5</td>
    <td class="tg-0pky">78.4</td>
    <td class="tg-0pky">55.2</td>
    <td class="tg-0pky">58.1</td>
    <td class="tg-0pky">74.0</td>
    <td class="tg-0pky">94.6</td>
    <td class="tg-0pky">62.3</td>
    <td class="tg-0pky">59.1</td>
    <td class="tg-0pky">65.1</td>
    <td class="tg-0pky">49.5</td>
    <td class="tg-0pky">52.4</td>
    <td class="tg-0pky">62.9</td>
    <td class="tg-0pky">47.7</td>
  </tr>
  <tr>
    <td class="tg-0pky"> lifting</td>
    <td class="tg-0pky">2017</td>
    <td class="tg-0pky">114</td>
    <td class="tg-0pky">54.2</td>
    <td class="tg-0pky">61.4</td>
    <td class="tg-0pky">60.2</td>
    <td class="tg-0pky">61.2</td>
    <td class="tg-0pky">79.4</td>
    <td class="tg-0pky">78.3</td>
    <td class="tg-0pky">63.1</td>
    <td class="tg-0pky">81.6</td>
    <td class="tg-0pky">70.1</td>
    <td class="tg-0pky">107.3</td>
    <td class="tg-0pky">69.3</td>
    <td class="tg-0pky">70.3</td>
    <td class="tg-0pky">74.3</td>
    <td class="tg-0pky">51.8</td>
    <td class="tg-0pky">63.2</td>
    <td class="tg-0pky">69.7</td>
    <td class="tg-0pky">-</td>
  </tr>
  <tr>
    <td class="tg-0pky"> lifting</td>
    <td class="tg-0pky">2017</td>
    <td class="tg-0pky">115</td>
    <td class="tg-0pky">54.8</td>
    <td class="tg-0pky">60.7</td>
    <td class="tg-0pky">58.2</td>
    <td class="tg-0pky">71.4</td>
    <td class="tg-0pky">62.0</td>
    <td class="tg-0pky">65.5</td>
    <td class="tg-0pky">53.8</td>
    <td class="tg-0pky">55.6</td>
    <td class="tg-0pky">75.2</td>
    <td class="tg-0pky">111.6</td>
    <td class="tg-0pky">64.2</td>
    <td class="tg-0pky">66.1</td>
    <td class="tg-0pky">51.4</td>
    <td class="tg-0pky">63.2</td>
    <td class="tg-0pky">55.3</td>
    <td class="tg-0pky">64.9</td>
    <td class="tg-0pky">-</td>
  </tr>
  <tr>
    <td class="tg-0pky"> lifting</td>
    <td class="tg-0pky">2018</td>
    <td class="tg-0pky">116</td>
    <td class="tg-0pky">51.5</td>
    <td class="tg-0pky">58.9</td>
    <td class="tg-0pky">50.4</td>
    <td class="tg-0pky">57.0</td>
    <td class="tg-0pky">62.1</td>
    <td class="tg-0pky">65.4</td>
    <td class="tg-0pky">49.8</td>
    <td class="tg-0pky">52.7</td>
    <td class="tg-0pky">69.2</td>
    <td class="tg-0pky">85.2</td>
    <td class="tg-0pky">57.4</td>
    <td class="tg-0pky">58.4</td>
    <td class="tg-0pky">43.6</td>
    <td class="tg-0pky">60.1</td>
    <td class="tg-0pky">47.7</td>
    <td class="tg-0pky">58.6</td>
    <td class="tg-0pky">37.7</td>
  </tr>
  <tr>
    <td class="tg-0pky"> lifting</td>
    <td class="tg-0pky">2018</td>
    <td class="tg-0pky">117</td>
    <td class="tg-0pky">49.2</td>
    <td class="tg-0pky">55.5</td>
    <td class="tg-0pky">53.6</td>
    <td class="tg-0pky">53.4</td>
    <td class="tg-0pky">63.8</td>
    <td class="tg-0pky">67.7</td>
    <td class="tg-0pky">50.2</td>
    <td class="tg-0pky">51.9</td>
    <td class="tg-0pky">70.3</td>
    <td class="tg-0pky">81.5</td>
    <td class="tg-0pky">57.7</td>
    <td class="tg-0pky">51.5</td>
    <td class="tg-0pky">58.6</td>
    <td class="tg-0pky">44.6</td>
    <td class="tg-0pky">47.2</td>
    <td class="tg-0pky">57.8</td>
    <td class="tg-0pky">42.9</td>
  </tr>
  <tr>
    <td class="tg-0pky"> lifting</td>
    <td class="tg-0pky">2019</td>
    <td class="tg-0pky">118</td>
    <td class="tg-0pky">34.4</td>
    <td class="tg-0pky">42.4</td>
    <td class="tg-0pky">36.6</td>
    <td class="tg-0pky">42.1</td>
    <td class="tg-0pky">38.2</td>
    <td class="tg-0pky">39.8</td>
    <td class="tg-0pky">34.7</td>
    <td class="tg-0pky">40.2</td>
    <td class="tg-0pky">45.6</td>
    <td class="tg-0pky">60.8</td>
    <td class="tg-0pky">39.0</td>
    <td class="tg-0pky">42.6</td>
    <td class="tg-0pky">42.0</td>
    <td class="tg-0pky">29.8</td>
    <td class="tg-0pky">31.7</td>
    <td class="tg-0pky">39.9</td>
    <td class="tg-0pky">27.9</td>
  </tr>
  <tr>
    <td class="tg-0pky"> lifting</td>
    <td class="tg-0pky">2019</td>
    <td class="tg-0pky">119</td>
    <td class="tg-0pky">54.0</td>
    <td class="tg-0pky">65.1</td>
    <td class="tg-0pky">58.5</td>
    <td class="tg-0pky">62.9</td>
    <td class="tg-0pky">67.9</td>
    <td class="tg-0pky">75.0</td>
    <td class="tg-0pky">54.0</td>
    <td class="tg-0pky">60.6</td>
    <td class="tg-0pky">82.7</td>
    <td class="tg-0pky">98.2</td>
    <td class="tg-0pky">63.3</td>
    <td class="tg-0pky">61.2</td>
    <td class="tg-0pky">66.9</td>
    <td class="tg-0pky">50.0</td>
    <td class="tg-0pky">56.5</td>
    <td class="tg-0pky">65.7</td>
    <td class="tg-0pky">49.2</td>
  </tr>
  <tr>
    <td class="tg-0pky"> lifting</td>
    <td class="tg-0pky">2019</td>
    <td class="tg-0pky">120</td>
    <td class="tg-0pky">43.8</td>
    <td class="tg-0pky">48.6</td>
    <td class="tg-0pky">49.1</td>
    <td class="tg-0pky">49.8</td>
    <td class="tg-0pky">57.6</td>
    <td class="tg-0pky">61.5</td>
    <td class="tg-0pky">45.9</td>
    <td class="tg-0pky">48.3</td>
    <td class="tg-0pky">62.0</td>
    <td class="tg-0pky">73.4</td>
    <td class="tg-0pky">54.8</td>
    <td class="tg-0pky">50.6</td>
    <td class="tg-0pky">56.0</td>
    <td class="tg-0pky">43.4</td>
    <td class="tg-0pky">45.5</td>
    <td class="tg-0pky">52.7</td>
    <td class="tg-0pky">42.6</td>
  </tr>
  <tr>
    <td class="tg-0pky"> lifting</td>
    <td class="tg-0pky">2019</td>
    <td class="tg-0pky">121</td>
    <td class="tg-0pky">48.6</td>
    <td class="tg-0pky">54.5</td>
    <td class="tg-0pky">54.2</td>
    <td class="tg-0pky">55.7</td>
    <td class="tg-0pky">62.6</td>
    <td class="tg-0pky">72.0</td>
    <td class="tg-0pky">50.5</td>
    <td class="tg-0pky">54.3</td>
    <td class="tg-0pky">70.0</td>
    <td class="tg-0pky">78.3</td>
    <td class="tg-0pky">58.1</td>
    <td class="tg-0pky">55.4</td>
    <td class="tg-0pky">61.4</td>
    <td class="tg-0pky">45.2</td>
    <td class="tg-0pky">49.7</td>
    <td class="tg-0pky">58.0</td>
    <td class="tg-0pky">-</td>
  </tr>
  <tr>
    <td class="tg-0pky"> lifting</td>
    <td class="tg-0pky">2019</td>
    <td class="tg-0pky">122</td>
    <td class="tg-0pky">46.8</td>
    <td class="tg-0pky">52.3</td>
    <td class="tg-0pky">44.7</td>
    <td class="tg-0pky">50.4</td>
    <td class="tg-0pky">52.9</td>
    <td class="tg-0pky">68.9</td>
    <td class="tg-0pky">49.6</td>
    <td class="tg-0pky">46.4</td>
    <td class="tg-0pky">60.2</td>
    <td class="tg-0pky">78.9</td>
    <td class="tg-0pky">51.2</td>
    <td class="tg-0pky">50.0</td>
    <td class="tg-0pky">54.8</td>
    <td class="tg-0pky">40.4</td>
    <td class="tg-0pky">43.3</td>
    <td class="tg-0pky">52.7</td>
    <td class="tg-0pky">42.2</td>
  </tr>
  <tr>
    <td class="tg-0pky"> lifting</td>
    <td class="tg-0pky">2019</td>
    <td class="tg-0pky">123</td>
    <td class="tg-0pky">47.3</td>
    <td class="tg-0pky">60.7</td>
    <td class="tg-0pky">51.4</td>
    <td class="tg-0pky">60.5</td>
    <td class="tg-0pky">61.1</td>
    <td class="tg-0pky">49.9</td>
    <td class="tg-0pky">47.3</td>
    <td class="tg-0pky">68.1</td>
    <td class="tg-0pky">86.2</td>
    <td class="tg-0pky">55.0</td>
    <td class="tg-0pky">67.8</td>
    <td class="tg-0pky">61.0</td>
    <td class="tg-0pky">42.1</td>
    <td class="tg-0pky">60.6</td>
    <td class="tg-0pky">45.3</td>
    <td class="tg-0pky">57.6</td>
    <td class="tg-0pky">-</td>
  </tr>
  <tr>
    <td class="tg-0pky">temporal</td>
    <td class="tg-0pky">2018</td>
    <td class="tg-0pky">124</td>
    <td class="tg-0pky">44.8</td>
    <td class="tg-0pky">50.4</td>
    <td class="tg-0pky">44.7</td>
    <td class="tg-0pky">49.0</td>
    <td class="tg-0pky">52.9</td>
    <td class="tg-0pky">61.4</td>
    <td class="tg-0pky">43.5</td>
    <td class="tg-0pky">45.5</td>
    <td class="tg-0pky">63.1</td>
    <td class="tg-0pky">87.3</td>
    <td class="tg-0pky">51.7</td>
    <td class="tg-0pky">48.5</td>
    <td class="tg-0pky">52.2</td>
    <td class="tg-0pky">37.6</td>
    <td class="tg-0pky">41.9</td>
    <td class="tg-0pky">52.1</td>
    <td class="tg-0pky">36.3</td>
  </tr>
  <tr>
    <td class="tg-0pky">temporal</td>
    <td class="tg-0pky">2019</td>
    <td class="tg-0pky">125</td>
    <td class="tg-0pky">45.2</td>
    <td class="tg-0pky">46.7</td>
    <td class="tg-0pky">43.3</td>
    <td class="tg-0pky">45.6</td>
    <td class="tg-0pky">48.1</td>
    <td class="tg-0pky">55.1</td>
    <td class="tg-0pky">44.6</td>
    <td class="tg-0pky">44.3</td>
    <td class="tg-0pky">57.3</td>
    <td class="tg-0pky">65.8</td>
    <td class="tg-0pky">47.1</td>
    <td class="tg-0pky">44.0</td>
    <td class="tg-0pky">49.0</td>
    <td class="tg-0pky">32.8</td>
    <td class="tg-0pky">33.9</td>
    <td class="tg-0pky">46.8</td>
    <td class="tg-0pky">36.5</td>
  </tr>
  <tr>
    <td class="tg-0pky">temporal</td>
    <td class="tg-0pky">2019</td>
    <td class="tg-0pky">126</td>
    <td class="tg-0pky">44.6</td>
    <td class="tg-0pky">47.4</td>
    <td class="tg-0pky">45.6</td>
    <td class="tg-0pky">48.8</td>
    <td class="tg-0pky">50.8</td>
    <td class="tg-0pky">59.0</td>
    <td class="tg-0pky">47.2</td>
    <td class="tg-0pky">43.9</td>
    <td class="tg-0pky">57.9</td>
    <td class="tg-0pky">61.9</td>
    <td class="tg-0pky">49.7</td>
    <td class="tg-0pky">46.6</td>
    <td class="tg-0pky">51.3</td>
    <td class="tg-0pky">37.1</td>
    <td class="tg-0pky">39.4</td>
    <td class="tg-0pky">48.8</td>
    <td class="tg-0pky">39.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">temporal</td>
    <td class="tg-0pky">2020</td>
    <td class="tg-0pky">128</td>
    <td class="tg-0pky">41.4</td>
    <td class="tg-0pky">43.5</td>
    <td class="tg-0pky">40.1</td>
    <td class="tg-0pky">42.9</td>
    <td class="tg-0pky">46.6</td>
    <td class="tg-0pky">51.9</td>
    <td class="tg-0pky">41.7</td>
    <td class="tg-0pky">42.3</td>
    <td class="tg-0pky">53.9</td>
    <td class="tg-0pky">60.2</td>
    <td class="tg-0pky">45.4</td>
    <td class="tg-0pky">41.7</td>
    <td class="tg-0pky">46.0</td>
    <td class="tg-0pky">31.5</td>
    <td class="tg-0pky">32.7</td>
    <td class="tg-0pky">44.1</td>
    <td class="tg-0pky">35.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">temporal</td>
    <td class="tg-0pky">2020</td>
    <td class="tg-0pky">129</td>
    <td class="tg-0pky">41.8</td>
    <td class="tg-0pky">44.8</td>
    <td class="tg-0pky">41.1</td>
    <td class="tg-0pky">44.9</td>
    <td class="tg-0pky">47.4</td>
    <td class="tg-0pky">54.1</td>
    <td class="tg-0pky">43.4</td>
    <td class="tg-0pky">42.2</td>
    <td class="tg-0pky">56.2</td>
    <td class="tg-0pky">63.6</td>
    <td class="tg-0pky">45.3</td>
    <td class="tg-0pky">43.5</td>
    <td class="tg-0pky">45.3</td>
    <td class="tg-0pky">31.3</td>
    <td class="tg-0pky">32.2</td>
    <td class="tg-0pky">45.1</td>
    <td class="tg-0pky">35.6</td>
  </tr>
  <tr>
    <td class="tg-0pky">Model-based methods</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">Protocol 1 MPJPE</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">Protocol   2 PMPJPE</td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">Approaches</td>
    <td class="tg-0pky">Year</td>
    <td class="tg-0pky">Methods</td>
    <td class="tg-0pky">Dir. </td>
    <td class="tg-0pky">Disc. </td>
    <td class="tg-0pky">Eat. </td>
    <td class="tg-0pky">Greet</td>
    <td class="tg-0pky"> Phone </td>
    <td class="tg-0pky">Photo </td>
    <td class="tg-0pky">Pose </td>
    <td class="tg-0pky">Purch.</td>
    <td class="tg-0pky"> Sit </td>
    <td class="tg-0pky">SitD. </td>
    <td class="tg-0pky">Somke </td>
    <td class="tg-0pky">Wait</td>
    <td class="tg-0pky"> WalkD. </td>
    <td class="tg-0pky">Walk</td>
    <td class="tg-0pky"> WalkT.</td>
    <td class="tg-0pky">Average</td>
    <td class="tg-0pky">Average</td>
  </tr>
  <tr>
    <td class="tg-0pky">SMPL</td>
    <td class="tg-0pky">2016</td>
    <td class="tg-0pky">130</td>
    <td class="tg-0pky">62.0</td>
    <td class="tg-0pky">60.2</td>
    <td class="tg-0pky">67.8</td>
    <td class="tg-0pky">76.5</td>
    <td class="tg-0pky">92.1</td>
    <td class="tg-0pky">77.0</td>
    <td class="tg-0pky">73.0</td>
    <td class="tg-0pky">75.3</td>
    <td class="tg-0pky">100.3</td>
    <td class="tg-0pky">137.3</td>
    <td class="tg-0pky">83.4</td>
    <td class="tg-0pky">77.3</td>
    <td class="tg-0pky">79.7</td>
    <td class="tg-0pky">86.8</td>
    <td class="tg-0pky">81.7</td>
    <td class="tg-0pky">69.3</td>
    <td class="tg-0pky">-</td>
  </tr>
  <tr>
    <td class="tg-0pky">SMPL</td>
    <td class="tg-0pky">2018</td>
    <td class="tg-0pky">131</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">59.9</td>
  </tr>
  <tr>
    <td class="tg-0pky">SMPL</td>
    <td class="tg-0pky">2019</td>
    <td class="tg-0pky">132</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">50.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">SMPL</td>
    <td class="tg-0pky">2019</td>
    <td class="tg-0pky">133</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">41.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">SMPL</td>
    <td class="tg-0pky">2019</td>
    <td class="tg-0pky">134</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">77.8</td>
    <td class="tg-0pky">54.3</td>
  </tr>
  <tr>
    <td class="tg-0pky">SMPL</td>
    <td class="tg-0pky">2019</td>
    <td class="tg-0pky">135</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">65.6</td>
    <td class="tg-0pky">41.4</td>
  </tr>
  <tr>
    <td class="tg-0pky">CylinderMan</td>
    <td class="tg-0pky">2019</td>
    <td class="tg-0pky">136</td>
    <td class="tg-0pky">38.3</td>
    <td class="tg-0pky">41.3</td>
    <td class="tg-0pky">46.1</td>
    <td class="tg-0pky">40.1</td>
    <td class="tg-0pky">41.6</td>
    <td class="tg-0pky">51.9</td>
    <td class="tg-0pky">41.8</td>
    <td class="tg-0pky">40.9</td>
    <td class="tg-0pky">51.5</td>
    <td class="tg-0pky">58.4</td>
    <td class="tg-0pky">42.2</td>
    <td class="tg-0pky">44.6</td>
    <td class="tg-0pky">41.7</td>
    <td class="tg-0pky">33.7</td>
    <td class="tg-0pky">30.1</td>
    <td class="tg-0pky">42.9</td>
    <td class="tg-0pky">32.8</td>
  </tr>
  <tr>
    <td class="tg-0pky">Adam </td>
    <td class="tg-0pky">2019</td>
    <td class="tg-0pky">137</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">58.3</td>
    <td class="tg-0pky">-</td>
  </tr>
  <tr>
    <td class="tg-0pky">Kinematic</td>
    <td class="tg-0pky">2018</td>
    <td class="tg-0pky">138</td>
    <td class="tg-0pky">43.8</td>
    <td class="tg-0pky">51.7</td>
    <td class="tg-0pky">48.8</td>
    <td class="tg-0pky">53.1</td>
    <td class="tg-0pky">52.2</td>
    <td class="tg-0pky">74.9</td>
    <td class="tg-0pky">52.7</td>
    <td class="tg-0pky">44.6</td>
    <td class="tg-0pky">56.9</td>
    <td class="tg-0pky">74.3</td>
    <td class="tg-0pky">56.7</td>
    <td class="tg-0pky">66.4</td>
    <td class="tg-0pky">47.5</td>
    <td class="tg-0pky">68.4</td>
    <td class="tg-0pky">45.6</td>
    <td class="tg-0pky">55.8</td>
    <td class="tg-0pky">46.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">Kinematic</td>
    <td class="tg-0pky">2019</td>
    <td class="tg-0pky">139</td>
    <td class="tg-0pky">44.7</td>
    <td class="tg-0pky">48.9</td>
    <td class="tg-0pky">47.0</td>
    <td class="tg-0pky">49.0</td>
    <td class="tg-0pky">56.4</td>
    <td class="tg-0pky">67.7</td>
    <td class="tg-0pky">48.7</td>
    <td class="tg-0pky">47.0</td>
    <td class="tg-0pky">63.0</td>
    <td class="tg-0pky">78.1</td>
    <td class="tg-0pky">51.1</td>
    <td class="tg-0pky">50.1</td>
    <td class="tg-0pky">54.5</td>
    <td class="tg-0pky">40.1</td>
    <td class="tg-0pky">43.0</td>
    <td class="tg-0pky">52.6</td>
    <td class="tg-0pky">40.7</td>
  </tr>
  <tr>
    <td class="tg-0pky">Kinematic</td>
    <td class="tg-0pky">2020</td>
    <td class="tg-0pky">140</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky">50.8</td>
  </tr>
  <tr>
    <td class="tg-0pky">Kinematic</td>
    <td class="tg-0pky">2020</td>
    <td class="tg-0pky">141</td>
    <td class="tg-0pky">37.4</td>
    <td class="tg-0pky">43.5</td>
    <td class="tg-0pky">42.7</td>
    <td class="tg-0pky">42.7</td>
    <td class="tg-0pky">46.6</td>
    <td class="tg-0pky">59.7</td>
    <td class="tg-0pky">41.3</td>
    <td class="tg-0pky">45.1</td>
    <td class="tg-0pky">52.7</td>
    <td class="tg-0pky">60.2</td>
    <td class="tg-0pky">45.8</td>
    <td class="tg-0pky">43.1</td>
    <td class="tg-0pky">47.7</td>
    <td class="tg-0pky">33.7</td>
    <td class="tg-0pky">37.1</td>
    <td class="tg-0pky">45.6</td>
    <td class="tg-0pky">36.2</td>
  </tr>
</tbody>
</table>

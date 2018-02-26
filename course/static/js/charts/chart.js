google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
var data = google.visualization.arrayToDataTable([
  ['Year', 'Текущий курс', 'Предсказание'],
  ['2013',  1000,		null],
  ['2014',  1170,      1060],
  ['2015',  660,       620],
  ['2016',  1030,      1040]
]);

var options = {
  title: course_name,
  hAxis: {title: 'Время',  titleTextStyle: {color: '#333'}},
  vAxis: {minValue: 0}
};

var chart = new google.visualization.AreaChart(document.getElementById('chart_div'));
chart.draw(data, options);
}
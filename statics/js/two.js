const ctx = document.getElementById("iot-chart");
var chartData = {
  type: "line",
  data: {
    labels: [1, 2, 3, 4, 5, 6],
    datasets: [
      {
        label: "IOT Data",
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1,
      },
    ],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
};
var myChart = new Chart(ctx, chartData);

var socket = new WebSocket("ws://localhost:8000/ws/two_url/");

socket.onmessage = function (event) {
  var data = JSON.parse(event.data);
  console.log(data);
  var newChartData = chartData.data.datasets[0].data;
  newChartData.shift();
  newChartData.push(data.data);
  chartData.data.datasets[0].data = newChartData;
  myChart.update();
};

"use strict"

const getById = (id) => {
    return document.getElementById(id)
}

let totalspend_week = 0, totalincome_week = 0;

//  function to calculate day
function createDay(day_number) {
    switch(day_number) 
    {
        case 1 : return "Monday";break;
        case 2 : return "Tuesday";break;
        case 3 : return "Wednesday";break;
        case 4 : return "Thursday";break;
        case 5 : return "Friday";break;
        case 6 : return "Saturday";break;
        case 0   : return "Sunday";break;
        default : return "Invalid day"
    }
}

const createBarChart = (ctx, labels, dataset_label, data) => {
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: dataset_label,
                data: data,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(130, 229, 32, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)',
                    'rgba(58, 122, 15, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}

var chart = getById('barchart') //  bar chart DOM 

function createXHR() {
    return new XMLHttpRequest() || new ActiveXObject('Microsoft.XMLHTTP')
}

function getBarGraphData() {
    let xhr = createXHR()

    xhr.onload = () => {
        
        if (xhr.status == 200) {

            let data = JSON.parse(xhr.responseText)
            let start_date = new Date(data.start_date), end_date = new Date(data.end_date);
            let start_day = parseInt(start_date.getDay()), end_day = parseInt(end_date.getDay());

            let labels = new Array();

            for (let i=1; i<=7; i++) {
                console.log(start_day)
                if(start_day == 7) start_day=0;
                labels.push(createDay(start_day++));
            }

            console.table(labels);

            let dataset = new Object()
            
            let transactions = JSON.parse(data.transactions)
            
            transactions.forEach(transaction => {
                let fields = transaction.fields
                
                let dayName = createDay(new Date(fields.date).getDay())
                
                if (fields.transaction_type == 'DB') {
                    totalspend_week+=fields.amount
                    if (dataset.hasOwnProperty(dayName)) {
                        dataset[dayName]+=fields.amount;
                    }else{
                        dataset[dayName]=fields.amount;
                    }
                }else{
                    totalincome_week+=fields.amount;
                }
            })

            let oset = new Array()

            for (let i=1;i<=7;i++) 
            {
                if (start_day==8) start_day=1;
                let day = createDay(start_day++)
                if (dataset.hasOwnProperty(day)) {
                    oset.push(dataset[day])
                }else{
                    oset.push(0)
                }
            }

            createBarChart(chart, labels, "Weekly transactions", oset);
            createPieChart(getById('piechart'));
            
        }
    }

    xhr.onloadstart = () => {
        chart.style.display = 'none';
    }

    xhr.onloadend = () => {
        chart.style.display = 'block';
        getById('spinner').style.display = 'none';
    }

    xhr.open('GET', 'http://127.0.0.1:8000/api/transaction/bargraph/', true);
    xhr.send();

}

function createPieChart(ctx, labels, dataset_label, data) {
    var myDoughnutChart = new Chart(ctx, {
        type: 'doughnut',
			data: {
				datasets: [{
					data: [
						totalspend_week, totalincome_week
					],
					backgroundColor: ['red','lightgreen'],
					label: 'Dataset 1'
				}],
				labels: [
					'Spent',
					'Income',
				]
			},
    });
}

function getPieChartData() 
{

}

window.addEventListener('DOMContentLoaded', () => {
    getBarGraphData();  //  bar graph function
});

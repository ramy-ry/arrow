
const dates = progressData.map(item => item.date);
const hours = progressData.map(item => item.hours);
const satisfaction = progressData.map(item => item.satisfaction);


//Neon Plugiin


const neonEffect = {

    id: "neonEffect",

    beforeDatasetDraw(chart) {

        const { ctx } = chart;

        ctx.save();

        ctx.shadowColor = chart.data.datasets[0].borderColor;
        ctx.shadowBlur = 3;

    },

    afterDatasetDraw(chart) {

        chart.ctx.restore();

    }

};



//the first


const ctx1 = document
    .getElementById("hoursChart")
    .getContext("2d");


const gradient1 = ctx1.createLinearGradient(0, 0, 0, 400);

gradient1.addColorStop(0, "rgba(255, 255, 255, 0.62)");
gradient1.addColorStop(0.5, "rgba(205, 214, 235, 0.15)");
gradient1.addColorStop(1, "rgba(181, 202, 255, 0)");




new Chart(ctx1, {

    type: "line",

    data: {

        labels: dates,

        datasets: [{

            label: "progress hours",

            data: hours,

            borderColor: "#ffffff",

            backgroundColor: gradient1,

            fill: true,

            borderWidth: 3,

            tension: 0.4,

            pointRadius: 5,

            pointHoverRadius: 10,

            pointBackgroundColor: "#ffffff"

        }]
    },

    plugins: [neonEffect]

});



//the second 




const ctx2 = document
    .getElementById("satisfactionChart")
    .getContext("2d");


const gradient2 = ctx2.createLinearGradient(0, 0, 0, 400);

gradient2.addColorStop(0, "rgba(255,255,255,0.4)");
gradient2.addColorStop(0.5, "rgba(255,255,255,0.1)");
gradient2.addColorStop(1, "rgba(255,255,255,0)");




new Chart(ctx2, {

    type: "bar",

    data: {

        labels: dates,

        datasets: [{

            label: "Mood",

            data: satisfaction,

            borderColor: "#ffffffea",

            backgroundColor: "#8f8f8fc9",

            borderWidth: 2,

            borderRadius:10,

            hoverBackgroundColor : "#d2d8dec9"

        }]
    },

});

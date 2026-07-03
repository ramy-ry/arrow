let currentDate ="";
document.addEventListener('DOMContentLoaded', function () {

    const calendarEl = document.getElementById('calendar');

    const calendar = new FullCalendar.Calendar(calendarEl, {

        initialView: 'dayGridMonth',

        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: ''
        },

        dateClick: function(info) {

    
    document.querySelectorAll(".selected-day").forEach(day => {
        day.classList.remove("selected-day");
    });

    
    info.dayEl.classList.add("selected-day");


    document.getElementById("date-input").value = info.dateStr;

    
    document.querySelector(".question-form").style.display = "block";
}

    });

    calendar.render();

});




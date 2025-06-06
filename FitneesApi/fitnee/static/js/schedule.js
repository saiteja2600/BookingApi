$(document).ready(function () {
    $('#calendar').fullCalendar({
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
        },
        events: {
            url: '/schedule', 
            type: 'GET',

            error: function () {
                alert('There was an error while fetching events!');
            }
        },
        
        
    });
});



$(document).ready(function () {
    $('.btn-delete').click(function (e) {
        e.preventDefault();
        const deleteUrl = $(this).data('delete-url'); // will now have the proper URL

        if (!deleteUrl) {
            console.error('No delete URL found!');
            return;
        }

        Swal.fire({
            title: 'Are you sure?',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#d33',
            cancelButtonColor: '#3085d6',
            confirmButtonText: 'Yes',
            cancelButtonText: 'No'
        }).then((result) => {
            if (result.isConfirmed) {
                window.location.href = deleteUrl;
            }
        });
    });
});

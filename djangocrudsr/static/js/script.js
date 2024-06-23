
    document.addEventListener('DOMContentLoaded', function () {
        var alerts = document.querySelectorAll('.custom-alert');
        alerts.forEach(function(alert) {
            setTimeout(function() {
                alert.style.opacity = '0';
                setTimeout(function() {
                    alert.remove();
                }, 500); // 500 milliseconds for fade out effect
            }, 3000); // 3000 milliseconds = 3 seconds
        });
    });



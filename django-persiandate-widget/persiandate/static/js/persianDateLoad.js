$(document).ready(function () {
            /*
             Default
             */
    if (!$('.observer').attr('data-used')) {
        window.pd = $("#inlineDatepicker").persianDatepicker({
            timePicker: {
                enabled: true
            },
            altField: '#inlineDatepickerAlt',
            altFormat: "YYYY MM DD HH:mm:ss",
            //            minDate:1258675200000,
            //            maxDate:1358675200000,
            checkDate: function (unix) {
                var output = true;
                var d = new persianDate(unix);
                if (d.date() == 20) {
                    output = false;
                }
                return output;
            },
            checkMonth: function (month) {
                var output = true;
                if (month == 1) {
                    output = false;
                }
                return output;

            }, checkYear: function (year) {
                var output = true;
                if (year == 1396) {
                    output = false;
                }
                return output;
            }

        }).data('datepicker');

        $("#inlineDatepicker").pDatepicker("setDate", [1391, 12, 1, 11, 14]);

        //pd.setDate([1333,12,28,11,20,30]);
        /*
         observer
         */
        $(".observer").persianDatepicker({
            altField: '.observerAlt',
            altFormat: "YYYY MM DD HH:mm:ss",
            observer: true,
            format: 'YYYY-MM-DD'

        });
        $(".observer").attr('data-used', 'used')
    }
});
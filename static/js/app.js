var select = document.getElementById('from');

function changeLabel() {
    document.getElementById("fromLabel").innerHTML = select.options[select.selectedIndex].value;
}

function addResult(theCurrency, theTotal, theDate) {
    document.getElementById("result").innerHTML = '<div class="card pt-2">' +
        '<h5>' + theCurrency + theTotal + '</h5>' +
        '<p style="font-size: 12px; color: gray;">Data on: ' + theDate + '</p>' +
        '</div>'
}

select.addEventListener('change', changeLabel, false);


$(document).ready(function () {
    $("#convert").click(function () {
        convert();
    });
});

function convert() {
    var from = $('#from').val();
    var to = $('#to').val();
    var total = $('#total').val();
    var url = '/convert/?' + 'from=' + from + "&to=" + to + "&total=" + total;

    $.ajax({
        url: url,
        success: function (data) {
            addResult(data['currency'], data['total'], data['date']);
        },
        fail: function (xhr, errorThrown) {
            alert('request failed');
        }
    });
}
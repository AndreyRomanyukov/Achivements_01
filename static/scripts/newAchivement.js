function init() {

}

$(document).on('click', '#btnCancel', function () {
    window.location.replace(hostUrl + "/");
});


$(document).on('click', '#btnNewAchivement', function () {
    var newAchivement = {};
    newAchivement.Title = $('#txtTitle').val();
    newAchivement.Description = $('#txtDescription').val();
    newAchivement.XTimes = $('#txtXTimes').val();
    newAchivement.ProgressCurrent = $('#txtProgressCurrent').val();
    newAchivement.ProgressEnd = $('#txtProgressEnd').val();
    newAchivement.Done = document.getElementById("chbDone").checked;

    dataProvider.insertAchivement(newAchivement, function (result) {
        alert(result.result)
    });
});
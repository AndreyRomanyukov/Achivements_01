var urlDataProvider = hostUrl + "/DataProvider";

var dataProvider = {
    getSimpleAnswer: function (callback) {
        $.ajax({
            type: "GET",
            url: urlDataProvider,
            data: {
                f: 'getSimpleAnswer',
            },
            dataType: 'json',
            success: function(result) {
                callback(result);
            },
            error: function(msg) {
                var errorMessage;
                errorMessage = msg.status + "\r\n";
                errorMessage += msg.statusText + "\r\n";
                errorMessage += msg.responseText + "\r\n";
                errorMessage += msg.errorThrown;
                alert("error" + errorMessage);
            }
        });
    },

    insertAchivement: function (newAchivement, callback) {
        $.ajax({
            type: "GET",
            url: urlDataProvider,
            data: {
                f: 'insertAchivement',
                title: newAchivement.Title,
                description: newAchivement.Description,
                xtimes: newAchivement.XTimes,
                progress_current: newAchivement.ProgressCurrent,
                progress_end: newAchivement.ProgressEnd,
                done: newAchivement.Done,
            },
            dataType: 'json',
            success: function(result) {
                callback(result);
            },
            error: function(msg) {
                var errorMessage;
                errorMessage = msg.status + "\r\n";
                errorMessage += msg.statusText + "\r\n";
                errorMessage += msg.responseText + "\r\n";
                errorMessage += msg.errorThrown;
                alert("error" + errorMessage);
            }
        });
    }
}
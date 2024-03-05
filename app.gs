function doGet(e) {

	var params = e.parameter;
	var SpreadSheet = SpreadsheetApp.openById("1CGzBVOT460e8rWHAe1jCbUZhm1BgBJIv22-AFUnK4HM");
	var Sheet = SpreadSheet.getSheets()[0];
	var LastRow = Sheet.getLastRow();

	Sheet.getRange(LastRow+1, 1).setValue(params.name);
	Sheet.getRange(LastRow+1, 2).setValue(params.mail);
	Sheet.getRange(LastRow+1, 3).setValue(params.formid);

	for (var i = 1; i <= 3; i++) {
		Sheet.getRange(LastRow+1, 3+i).setValue(params["q" + i.toString()]);
	}
    console.log("done")
	return ContentService.createTextOutput(params.thank);
}
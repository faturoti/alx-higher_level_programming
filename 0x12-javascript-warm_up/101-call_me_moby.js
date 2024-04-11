#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
	for (let n = 0; n < x; n++){
		theFunction();
	}
};

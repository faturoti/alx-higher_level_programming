#!/usr/bin/node
exports.esrever = function (list) {
	let rev = [];
	for (let n = list.length - 1; n > 0; n--){
		rev[list.length - 1 - n] = list[n];
	}

	return rev;
};

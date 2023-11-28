#!/usr/bin/node
exports.converter = function (base) { return num => num.toString(base); };
// handled the case where undefined
// tried logical OR (||) to provide an empty string when undefined
// used num as the passed var instead of using argv.

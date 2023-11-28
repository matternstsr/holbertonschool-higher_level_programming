#!/usr/bin/node
exports.converter = function (base) { return (process.argv[2] || '').toString(base); };
// handled the case where undefined
// tried logical OR (||) to provide an empty string when undefined

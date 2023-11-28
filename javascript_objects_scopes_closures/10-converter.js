#!/usr/bin/node
exports.converter = function (base) {
    return process.argv[2].toString(base); };

#!/usr/bin/node
exports.callMeMoby = function callMeMoby (x, theFunction) {
  for (let idx = 0; idx < x; idx++) {
    theFunction();
  }
};

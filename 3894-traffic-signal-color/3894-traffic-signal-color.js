/**
 * @param {number} timer
 * @return {string}
 */
var trafficSignal = function(timer) {
    if (timer<=90 && timer>30){
        return "Red";
    }else if (timer===30){
        return "Orange";
    }else if (timer===0){
        return "Green";
    }else{
        return "Invalid";
    }
};
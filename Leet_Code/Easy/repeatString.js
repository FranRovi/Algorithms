// Leet Code Algo 2796. Repeat String

/**
 * @param {number} times
 * @return {string}
 */

String.prototype.replicate = function(times) {
    let answer = ''
    for (i = 0; i<times; i++) {
        answer += this;
    }
    return answer    
}


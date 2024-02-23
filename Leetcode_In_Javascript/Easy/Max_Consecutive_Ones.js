/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    var greatest_count = 0
    count = 0
    for (num of nums) {
        if (num === 1) {
            count += 1
        }
        else {
            count = 0
        }
        if (count > greatest_count) {
            greatest_count = count
        }
    }
    return greatest_count

};
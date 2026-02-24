// function to check whether mid speed is enough
// to eat all piles of bananas under k hours
function check(arr, mid, k) {
    let totalHours = 0;
    for (let i = 0; i < arr.length; i++) {
        totalHours += Math.floor((arr[i] + mid - 1) / mid);
    }

    // return true if required time is less than 
    // or equals to given hour, otherwise return false
    return totalHours <= k;
}

function kokoEat(arr, k) {
    // minimum speed of eating is 1 banana/hours
    let lo = 1;

    // maximum speed of eating is 
    // the maximum bananas in given piles
    let hi = Math.max(...arr);
    let res = hi;

    while (lo <= hi) {
        let mid = lo + Math.floor((hi - lo) / 2);

        // check if the mid(hours) is valid
        if (check(arr, mid, k) === true) {
          
            // if valid continue to search at
            // lower speed
            hi = mid - 1;
            res = mid;
        }
        else {
          
            // if cant finish bananas in given
            // hours, then increase the speed
            lo = mid + 1;
        }
    }
    return res;
}

// Driver Code
let arr = [5, 10, 3];
let k = 4;
console.log(kokoEat(arr, k));


          

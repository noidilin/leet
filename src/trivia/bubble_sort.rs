// trivia/bubble_sort.rs
//
// Educational bubble sort skeleton.
// Goal: translate the Python version into Rust without jumping straight to
// the final answer.

pub fn bubble_sort(mut nums: Vec<i32>) -> Vec<i32> {
    // Framework:
    // 1. Track whether a pass made any swap.
    // 2. Track the current unsorted end boundary.
    // 3. Compare adjacent values from left to right.
    // 4. Swap when the left value is bigger.
    // 5. After each pass, shrink the end boundary by 1.
    // 6. Stop early when a full pass makes no swaps.

    if nums.len() < 2 {
        return nums;
    }

    let mut swapping = true;
    let mut end = nums.len();

    while swapping {
        swapping = false;

        for i in 1..end {
            if nums[i - 1] > nums[i] {
                nums.swap(i - 1, i);
                swapping = true;
            }
        }
        end -= 1;
    }

    nums
}

#[cfg(test)]
mod tests {
    use super::bubble_sort;

    #[test]
    fn sorts_basic_case() {
        let nums = vec![5, 1, 4, 2, 8];
        assert_eq!(bubble_sort(nums), vec![1, 2, 4, 5, 8]);
    }

    #[test]
    fn keeps_sorted_input() {
        let nums = vec![1, 2, 3, 4];
        assert_eq!(bubble_sort(nums), vec![1, 2, 3, 4]);
    }
}

// WTF JS
function checkIfExist(arr: number[]): boolean {
    const seen = new Set<number>();
    for (let i = 0; i < arr.length; i++) {
        if (seen.has(arr[i] * 2) || seen.has(arr[i] / 2)) {
            return true;
        }
        seen.add(arr[i]);
    }
    return false;
};
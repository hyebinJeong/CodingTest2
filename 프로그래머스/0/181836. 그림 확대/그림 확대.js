function solution(picture, k) {
    const answer = [];

    for (const row of picture) {
        let enlargedRow = "";
        for (const ch of row) {
            enlargedRow += ch.repeat(k);
        }

        for (let i = 0; i < k; i++) {
            answer.push(enlargedRow);
        }
    }

    return answer;
}
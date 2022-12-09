const fs = require('fs');
const path = require('path');

function readFile() {
  // const filePath = path.join(__dirname, 'example');
  const filePath = path.join(__dirname, 'day8');

  return fs.readFileSync(filePath, { encoding: 'utf-8' })
    .toString()
    .split('\n')
    .map((row) => row.split('')
      .map((value) => parseInt(value, 10)));
}

function findTallTrees1(coll) {
  let maxVal = coll[0];

  const out = [];

  for (let i = 1; i < coll.length - 1; i += 1) {
    if (coll[i] > maxVal) {
      maxVal = coll[i];
      out.push(i);
    }
  }

  return out;
}

function processRows(matrix) {
  const res = [];

  for (let i = 1; i < matrix.length - 1; i += 1) {
    const row = [...matrix[i]];

    const searchFRes = findTallTrees1(row);
    while (searchFRes.length > 0) {
      const newItem = [i, searchFRes.pop()];

      res.push(newItem.toString());
    }

    const searchBRes = findTallTrees1([...row].reverse());
    while (searchBRes.length > 0) {
      const newItem = [i, row.length - searchBRes.pop() - 1];

      res.push(newItem.toString());
    }
  }

  return res;
}

function processColumns(matrix) {
  const res = [];

  for (let i = 1; i < matrix[0].length - 1; i += 1) {
    const column = [...matrix.map((value) => value[i])];

    const searchFRes = findTallTrees1(column);
    while (searchFRes.length > 0) {
      res.push([searchFRes.pop(), i].toString());
    }

    const searchBRes = findTallTrees1([...column].reverse());
    while (searchBRes.length > 0) {
      res.push([column.length - searchBRes.pop() - 1, i].toString());
    }
  }

  return res;
}

function part1() {
  const matrix = readFile();

  const rows = matrix.length;
  const columns = matrix[0].length;

  let res = [];

  res = res.concat(processRows(matrix));
  res = res.concat(processColumns(matrix));
  res = Array.from(new Set(res));

  return 2 * rows + 2 * (columns - 2) + res.length;
}

function findTallTrees2(coll) {
  let lastMaxVal = coll[0];
  let foundGte = false;
  const out = [];

  for (let i = 1; i < coll.length; i += 1) {
    if (coll[i] <= lastMaxVal && !foundGte) {
      out.push(i);
    }

    if (coll[i] > lastMaxVal) {
      lastMaxVal = coll[i];
      out.push(i);
    }

    if (coll[i] >= coll[0]) {
      foundGte = true;
    }
  }

  return out;
}

function calcScore(matrix, r, c) {
  const top = [...matrix.slice(0, r + 1).map((value) => value[c])].reverse();
  const left = [...matrix[r].slice(0, c + 1)].reverse();
  const down = [...matrix.slice(r).map((value) => value[c])];
  const right = [...matrix[r].slice(c)];

  const topScore = findTallTrees2(top);
  const leftScore = findTallTrees2(left);
  const downScore = findTallTrees2(down);
  const rightScore = findTallTrees2(right);

  const out = Math.max(1, topScore.length)
        * Math.max(1, leftScore.length)
        * Math.max(1, downScore.length)
        * Math.max(1, rightScore.length);

  return out;
}

function part2() {
  const matrix = readFile();

  const rows = matrix.length;
  const columns = matrix[0].length;

  const res = [];

  for (let i = 0; i < rows; i += 1) {
    for (let j = 0; j < columns; j += 1) {
      res.push(calcScore(matrix, i, j));
    }
  }

  return Math.max(...res);
}

console.log(part1());
console.log(part2());

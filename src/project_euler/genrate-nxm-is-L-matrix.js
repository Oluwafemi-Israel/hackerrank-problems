var numbers = prompt('Enter comma seperated numbers: ');
numbers = numbers.split(',').map(Number);

function get_matrix_dimension(numbers){
  if(numbers.length==1){
    return {rows: 1, cols: 1};
  }

  for(var n=2; n<=numbers.length; n++){
    if(numbers.length%n===0){
      return {rows: n, cols: numbers.length/n};
    }
  }
}

function generate_matrix(numbers, dimension){
  console.log('Generating a '+dimension.rows+'x'+dimension.cols+' matrix');

  var result = [];
  for(var i=0; i<numbers.length; i+=dimension.cols){
    result.push(numbers.slice(i, i+dimension.cols));
  }
  return result;
}

dimension = get_matrix_dimension(numbers);
result = generate_matrix(numbers, dimension);
console.log(result);
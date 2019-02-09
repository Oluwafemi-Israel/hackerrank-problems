function getEncryptedText(plain_text){
  var shifted_ascii_vals= [];
  var cypher_text = [];

  for(var i in plain_text.split('')){
    shifted_ascii_vals.push(plain_text[i].charCodeAt()+5);
  }
  
  for(var j in shifted_ascii_vals){
    cypher_text.push(String.fromCharCode(shifted_ascii_vals[j]));
  }

  return cypher_text.join('');
}

function getDecryptedText(cypher_text){
  var ascii_vals= [];
  var plain_text = [];

  for(var i in cypher_text.split('')){
    ascii_vals.push(cypher_text[i].charCodeAt()-5);
  }

  for(var j in ascii_vals){
    plain_text.push(String.fromCharCode(ascii_vals[j]));
  }

  return plain_text.join('');
}


cypher_text = getEncryptedText(prompt('Enter the plain text to encrpyt: '));
console.log('Cypher text: '+cypher_text);

plain_text = getDecryptedText(prompt('Enter the cypher text to decrypt: '));
console.log('Plain text: '+plain_text);
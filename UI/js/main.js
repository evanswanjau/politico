// function to register user
function signupUser(){

    // authenticate first name
    if (document.forms["myForm"]["fname"].value == "") {
      document.getElementById('responseMessage').innerHTML = "first name is required";
      document.getElementById('responseMessage').style.display = 'block';
    }else {
      fname = document.forms["myForm"]["fname"].value;

      // authenticate second name
      if (document.forms["myForm"]["sname"].value == "") {
        document.getElementById('responseMessage').innerHTML = "second name is required";
        document.getElementById('responseMessage').style.display = 'block';
      }else {
        sname = document.forms["myForm"]["sname"].value;

        // authenticate id
        if (document.forms["myForm"]["nationalid"].value == "") {
          document.getElementById('responseMessage').innerHTML = "national ID is required";
          document.getElementById('responseMessage').style.display = 'block';
        }else {

          // authenticate size
          if (document.forms["myForm"]["nationalid"].value.length < 8 || document.forms["myForm"]["nationalid"].value.length > 8) {
            document.getElementById('responseMessage').innerHTML = "national ID must be equal to 8 characters";
            document.getElementById('responseMessage').style.display = 'block';
          }else{

          // authenticate integers only
          let idValues = document.forms["myForm"]["nationalid"].value.toLowerCase()

          if (isNaN(idValues) == true) {
            document.getElementById('responseMessage').innerHTML = "national ID must only contain integers";
            document.getElementById('responseMessage').style.display = 'block';
          }else {
            nationalid = document.forms["myForm"]["nationalid"].value;

            // authenticate password
            if (document.forms["myForm"]["password"].value == "") {
              document.getElementById('responseMessage').innerHTML = "password is required";
              document.getElementById('responseMessage').style.display = 'block';
            }else {
              if (document.forms["myForm"]["password"].value.length < 7) {
                document.getElementById('responseMessage').innerHTML = "password cannot be less than 7 charachters";
                document.getElementById('responseMessage').style.display = 'block';
              }else {
                if (document.forms["myForm"]["confirm-password"].value == "") {
                  document.getElementById('responseMessage').innerHTML = "please confirm your password";
                  document.getElementById('responseMessage').style.display = 'block';
                }else {
                  if (document.forms["myForm"]["confirm-password"].value != document.forms["myForm"]["password"].value) {
                    document.getElementById('responseMessage').innerHTML = "passwords are not similar";
                    document.getElementById('responseMessage').style.display = 'block';
                  }else {
                    password = document.forms["myForm"]["password"].value;
                    
                    document.getElementById('responseMessage').innerHTML = "registration successful";
                    document.getElementById('responseMessage').style.display = 'block';
                    document.getElementById('responseMessage').style.backgroundColor = '#1C855E';

                  }
                }
              }
            }
          }
        }
      }
    }
  }

	return false;
}

// function to sign in user
function signinUser(){

  // authenticate national id
  if (document.forms["myForm"]["nationalid"].value == "") {
    document.getElementById('responseMessage').innerHTML = "national ID is required";
    document.getElementById('responseMessage').style.display = 'block';
  }else {
    let nationalid = document.forms["myForm"]["nationalid"].value;

    // authenticate password
    if (document.forms["myForm"]["password"].value == "") {
      document.getElementById('responseMessage').innerHTML = "password is required";
      document.getElementById('responseMessage').style.display = 'block';
    }else {
      let password = document.forms["myForm"]["password"].value;

      document.getElementById('responseMessage').innerHTML = "login successful";
      document.getElementById('responseMessage').style.display = 'block';
      document.getElementById('responseMessage').style.backgroundColor = '#1C855E';
    }
  }

  return false;
}
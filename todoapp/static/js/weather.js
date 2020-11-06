    var button1= document.querySelector('.submit');
    var cname = document.querySelector('.name');
    var mintemp = document.querySelector('.mintemp');
    var maxtemp = document.querySelector('.maxtemp');
    var desc = document.querySelector('.description');
    var humidity = document.querySelector('.humidity');
    var pressure = document.querySelector('.pressure');
    button1.addEventListener('click', function(){
        fetch('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=0941ecd2acfb0f26b09f7b3ddbb438cf')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            var nameValue = data['name'];
            var mintempValue = data['main']['temp_min'];
            var maxtempValue = data['main']['temp_max'];
            var descValue = data['weather'][0]['description'];
            var humidityValue = data['main']['humidity'];
            var pressureValue = data['main']['pressure'];
            cname.innerHTML = "Country name - " + nameValue;
            mintemp.innerHTML = "Minimum Temperature - "+ mintempValue+" C";
            maxtemp.innerHTML = "Maximum Temperature - "+ maxtempValue+" C";
            desc.innerHTML = "Description - "+ descValue;
            humidity.innerHTML = "Humidity - "+ humidityValue;
            pressure.innerHTML = "Pressure - "+ pressureValue;
            input.value ="";
            $(".weather").show();
        })
        .catch(err => {
          alert("Wrong city name!")
          input.value="";
        });
    })
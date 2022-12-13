![azure1](https://user-images.githubusercontent.com/88910492/206944405-e82cd1a2-2642-4616-92d8-3cfe99223758.png)

This github readme describes and documents the Azure function part of my project which gets the information from [Openweathermap API](https://api.openweathermap.org), parses the relevant data and stores the results in cosmosDB. This data is then used by PowerBI to visualize the data. This readme does not contain any documentation for the PowerBI part.

# Table of Contents
- [Overview](https://github.com/Kotik112/Azure-timerTrigger-function/new/master?readme=1#azure-function-for-openweathermap-api)
- [Dependencies](https://github.com/Kotik112/Azure-timerTrigger-function/new/master?readme=1#dependencies)
- [Inputs](https://github.com/Kotik112/Azure-timerTrigger-function/new/master?readme=1#inputs)
- [Outputs](https://github.com/Kotik112/Azure-timerTrigger-function/new/master?readme=1#outputs)
- [Error Handling](https://github.com/Kotik112/Azure-timerTrigger-function/new/master?readme=1#error-handling)

# Azure Function for OpenWeatherMap API
This Azure function is triggered by a timer and makes an API call to the OpenWeatherMap API to get the current weather data for a specific location. It then extracts the temperature, humidity, and pressure data and writes it to an output binding.

## Dependencies
This function depends on the following libraries:

- `datetime`: Used to extract and format the date/time data from the API response.
- `requests`: Used to make the API call to the OpenWeatherMap API.

## Inputs
The function takes two inputs:

- `mytimer`: A timer trigger that specifies when the function should be executed.
  - For this project I set the execution interval to 3 minutes by specifying the cronjob timer "*/3 * * * *"
- `outdoc`: An output binding that specifies where the data from the API call should be written to.

## Outputs
The function writes the extracted weather data to the specified output binding as a JSON document with the following fields:

- `temp`: The current temperature in Celsius.
- `humidity`: The current humidity level in percent.
- `pressure`: The current pressure in millibars.
- `datetime`: The date and time when the data was collected, in Unix timestamp format.

## Error Handling
If there is an error while making the API call or writing the data to the output binding, the function will log the error message and continue execution.

## Troubleshooting
If the Azure function seems to work while it's running in `debug mode` (locally) and then complains about the `AzureCosmosDbString`, this is because when you are running the function locally, the function grabs the necessary environment variables from your `local.settings.json`. However, to run youu function in Azure cloud, you need to add the `AzureCosmosDbString` to your Azure function's `Application Settings`.
![azure-func](https://user-images.githubusercontent.com/88910492/207276474-ced494b2-596a-4e2c-9df9-6d6317d9dc97.png)

You can also add this from the [Azure function](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions) extention to VS code by Adding a new string or uploading your local settings.
![azure-func2](https://user-images.githubusercontent.com/88910492/207277113-e7673450-65c8-4f70-ae90-41d3d596144a.png)

/**
 * Helper-Function to generate a color scheme for a chart. This needs to be wrapped in a loop and be called for each
 * data point separately. <br>
 * Returns a string formatted as following: <br>
 * rgb(RED_VALUE, GREEN_VALUE, BLUE_VALUE)
 *
 * @param {number} index The index of the data point for which the color is generated.
 * @param {number} length The total amount of data points for which to generate colors.
 * @param {number} redBias Value between 0 and 1
 * @param {number} greenBias Value between 0 and 1
 * @param {number} blueBias Value between 0 and 1
 * @returns {string}
 */
function colorGenerator(index, length, redBias, greenBias, blueBias) {
    const red = redBias * (255 - index * (255 / length) + (255 / length));
    const green = greenBias * (255 - index * (255 / length) + (255 / length));
    const blue = blueBias * (255 - index * (255 / length) + (255 / length));
    return `rgb(${red},${green},${blue})`;
}
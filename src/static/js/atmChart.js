/**
 *
 * @param {array} apiData
 * @param {string} canvasID
 * @param {number} minimumAmountOfOccurrences
 * @param {number} redBias
 * @param {number} greenBias
 * @param {number} blueBias
 * @param {string|null} canton
 * @returns {bn}
 */
function createATMChart(
    apiData,
    canvasID,
    minimumAmountOfOccurrences = 10,
    redBias = 0.1,
    greenBias = 0.5,
    blueBias = 0.9,
    canton = null,
) {
    const labels = apiData.map(entry => {
        return entry['operator'];
    });

    const operator_occurrences = {};
    labels.forEach(operator => {
        if (operator in operator_occurrences) {
            operator_occurrences[operator] += 1
        } else {
            operator_occurrences[operator] = 1
        }
    });

    // Extract operator label and amount of each operator.
    const label_chart = [];
    const data_chart = [];
    for (const operator in operator_occurrences) {
        const occurrences = operator_occurrences[operator];
        if (occurrences >= minimumAmountOfOccurrences) {
            label_chart.push(operator);
            data_chart.push(occurrences);
        }
    }

    // Sort Data, so that Operators are descending
    const sorted_operators = label_chart.map(function (operator, occurrence) {
        return {
            label: operator,
            //The OR-Operator : ||  is there to prevent a failure in case of no available database. 0 would be handed over
            data: data_chart[occurrence] || 0
        };
    });

    const sorted_operator_data = sorted_operators.sort(function (occurrence_a, occurrence_b) {
        return occurrence_b.data > occurrence_a.data;
    });

    const sorted_labels = [];
    const sorted_occurrences = [];
    sorted_operator_data.forEach(function (operator) {
        sorted_labels.push(operator.label);
        sorted_occurrences.push(operator.data);
    });

    // Create the color scheme (light blue to dark blue)
    const color = [];
    for (const index in Object.keys(label_chart)) {
        color.push(colorGenerator(index, Object.keys(label_chart).length, redBias, greenBias, blueBias));
    }

    // content for Bar-Chart
    const config_data = {
        labels: sorted_labels,
        datasets: [{
            label: 'Anzahl Bankautomaten',
            backgroundColor: color,
            borderColor:
                'rgb(255, 99, 132)',
            data: sorted_occurrences,
        }]
    };

    // Creates the configuration for the bar chart.
    const config = {
        type: 'bar',
        data: config_data,
        options: {
            scales: {
                x: {
                    grid: {
                        display: true
                    }
                },
                y: {
                    grid: {
                        display: false
                    }
                }
            },
            responsive: true,
            maintainAspectRation: false,
            indexAxis: 'y',
            plugins: {
                legend: {
                    display: false,
                    labels: {
                        color: 'rgb(255, 99, 132)'
                    }
                }
            }
        },
    };

    const chart = new Chart(
        document.getElementById(canvasID),
        config
    );

    // Onclick implementation in the Bar Chart with redirection to Operator
    chart.canvas.onclick = (event) => {
        const activeElement = chart.getElementsAtEventForMode(event, 'nearest', {intersect: true}, true);
        if (activeElement.length > 0) {
            const clickedElementIndex = activeElement[0].index;
            const clickedLabel = sorted_labels[clickedElementIndex];

            const cantonSuffix = canton !== null ? `/${canton}` : ''
            window.location.href = `/map/${clickedLabel}${cantonSuffix}`;
        }
    }
    return chart;
}
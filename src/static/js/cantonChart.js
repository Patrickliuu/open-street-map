/**
 * Initializes the dynamic functionality of the canton.html.
 */
function init() {
    let chart = null;
    let cantonSearch = document.getElementById('canton-search');
    cantonSearch.value = "";
    cantonSearch.focus();

    const cantons = [
        "Aargau",
        "Appenzell Ausserrhoden",
        "Appenzell Innerrhoden",
        "Basel-Landschaft",
        "Basel-Stadt",
        "Bern",
        "Freiburg",
        "Genf",
        "Glarus",
        "Graubünden",
        "Jura",
        "Luzern",
        "Neuenburg",
        "Nidwalden",
        "Obwalden",
        "Sankt Gallen",
        "Schaffhausen",
        "Schwyz",
        "Solothurn",
        "Tessin",
        "Thurgau",
        "Uri",
        "Waadt",
        "Wallis",
        "Zug",
        "Zürich"
    ];

    cantonSearch.addEventListener('input', async (event) => {
        chart = await handleCantonSearchEvent(event, chart, cantons)
    });

    populateCantonPreview(cantons);
}

/**
 * Checks whether the string that the user searched for matches any cantons.
 * If it matches more than one canton, these cantons are displayed in the cantons-preview and are clickable.
 * If it matches exactly one canton, the bar-chart of ATMs is displayed for that canton.
 * If it matches no canton, an error message is displayed.
 *
 * @param {Event} event
 * @param {bn} chart
 * @param {String[]} cantons
 * @returns {Promise<bn>}
 */
async function handleCantonSearchEvent(event, chart, cantons) {
    const searchedString = event.target.value;
    const matchingCantons = cantons.filter((actualCanton) => {
        return actualCanton.toLowerCase().includes(searchedString.toLowerCase());
    });

    const cantonPreview = document.getElementById('cantons-preview');
    const errorElement = document.getElementById('canton-error-message');

    cantonPreview.innerHTML = "";
    errorElement.innerHTML = "";

    // No canton found.
    if (matchingCantons.length === 0) {
        if (chart !== null) {
            chart.clear();
            chart.destroy();
        }
        errorElement.innerHTML = "Es wurde kein Kanton mit diesem Namen gefunden."

        // null = chart doesn't exists (anymore).
        return null;
    }

    // Multiple cantons match the search term. (E.g. "Walden" => ["Obwalden", "Nidwalden"])
    if (matchingCantons.length > 1) {
        populateCantonPreview(matchingCantons);
        if (chart !== null) {
            // Clear the canvas.
            chart.clear();
            // Remove all event handlers on the chart.
            chart.destroy();
        }
        // null = chart doesn't exists (anymore).
        return null;
    }

    // We only get to this point, if exactly one canton matches the string that the user typed.
    const matchedCanton = matchingCantons[0];

    /*
    * Only re-create the chart if it doesn't exist already.
    * We need this to avoid re-drawing the canvas everytime the user enters a character.
    * For example when the user enters "Zü", it is already clear that they mean "Zürich", therefore the chart is
    * already drawn.
    * If they were to continue typing, the chart would be redrawn 4 more times. ("Zür", "Züri", "Züric", "Zürich")
    */
    if (chart === null) {
        const api = new APIHandler();
        const data = await api.fetchATMsByCanton(matchedCanton);

        // This should theoretically never be the case, since all cantons have data. Nevertheless, it is good to handle
        // it properly, in case the database would be empty for some reason.
        const cantonColor = randomCantonColorGenerator(matchedCanton);
        if (data.length > 0) {
            chart = createATMChart(
                data,
                'canton-canvas',
                0,
                cantonColor[0],
                cantonColor[1],
                cantonColor[2],
                matchedCanton
            );
        } else {
            errorElement.innerHTML = `Für den Kanton ${matchedCanton} sind keine Bankautomaten in der Datenbank verfügbar.`;
        }
    }
    return chart;
}

/**
 * Generates a set of three values between 0 and 1. (Red, Green and Blue)
 * Before calling Math.random() it uses David Bau's Math.seedrandom(<string>) function in order to get the same
 * color for the same canton every time.
 * For more information on the library: http://davidbau.com/archives/2010/01/30/random_seeds_coded_hints_and_quintillions.html#more
 *
 * @param canton
 */
function randomCantonColorGenerator(canton) {
    Math.seedrandom("seed_" + canton);
    return [
        Math.random(),
        Math.random(),
        Math.random(),
    ]
}

/**
 *
 * @param cantons
 */
function populateCantonPreview(cantons) {
    const cantonPreview = document.getElementById('cantons-preview');

    for (let canton of cantons) {
        let newElement = document.createElement('li');
        newElement.addEventListener('click', (_) => {
            const cantonSearch = document.getElementById('canton-search');
            cantonSearch.value = canton;
            cantonSearch.dispatchEvent(new Event('input'));
        });
        newElement.innerHTML = canton;
        cantonPreview.appendChild(newElement);
    }
}

init();
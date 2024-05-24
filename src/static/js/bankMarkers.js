/**
 * Creates and gets the correct icons for every bank operator.
 *
 * @param {string} fileName A string that is the same as the operator name.
 * @returns {L.icon} with operator_name of the chosen bank-operator
 */
async function getMarkerIcon(fileName) {
    const logoPath = `/static/logos/${fileName}.png`;
    if (await fileExists(window.location.host + logoPath)) {
        return L.icon({
            iconUrl: logoPath,
            name: {operator_name: fileName},
            iconSize: [25, 25], // size of the icon
            iconAnchor: [12.5, 12.5], // Which pixel of the icon should be fixed to the actual longitude / latitude.
            popupAnchor: [-3, -76], // Point from which the popup should open relative to the iconAnchor
        });
    } else {
        return null;
    }

}

/**
 * Checks whether the given URL exists on the server.
 * TODO: This is probably a bad solution since it causes additional network traffic. However, I do not see a way of
 *   improving it, without removing the custom icons for the bank operators.
 *
 * @param url
 * @returns {Promise<boolean>}
 */
async function fileExists(url) {
    try {
        const response = await fetch('http://' + url);

        if (response.status !== 200) {
            return false;
        }
    } catch (e) {
        return false;
    }
    return true;
}

/**
 * Finds all longitude and latitude of the selected bank operators and places the markers on the map.
 *
 * @param {string} operatorName The name of the bank operator
 * @param {string|null} canton
 * @returns {L.marker} for all selected items with longitude and latitude (or {map} with markers?)
 */
async function placeBankMarkersForOperator(operatorName, canton = null) {
    const api = new APIHandler();
    const atms = await api.fetchATMsByOperator(operatorName, canton);
    const logo = await getMarkerIcon(operatorName);


    for (const atm of atms) {
        L.marker([atm.lat, atm.lon], logo ? {icon: logo} : null).addTo(map);
    }
}

// Note: The variable operatorName is a dynamic variable that is retrieved from the site URL
placeBankMarkersForOperator(operatorName, canton);
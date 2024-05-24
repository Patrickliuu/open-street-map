const SERVER_URL = 'http://127.0.0.1:14032/api/atm'

/**
 * This is a helper class to make API calls to any available API routes.
 */
class APIHandler {
    constructor(serverURL = null) {
        this.serverURL = serverURL == null ? SERVER_URL : serverURL;
    }

    /**
     * Makes an API call to the Flask server and returns the data received or throws an error if the server responds with
     * anything other than status-code 200.
     *
     * @returns {Promise<any>}
     */
    async fetchATMs() {
        const response = await fetch(this.serverURL);
        if (response.status === 200) {
            return await response.json();
        }
        throw `${this.serverURL}: Server responded with non-200 code!`
    }

    /**
     * Makes an API call to the Flask server using the operator name as a GET parameter and returns the data received
     * or throws an error if the server responds with anything other than status-code 200.
     *
     * @param {string} operatorName
     * @param {string|null} canton
     * @returns {Promise<any>}
     */
    async fetchATMsByOperator(operatorName, canton = null) {
        const cantonSuffix = canton !== "null" ? `/${canton}` : ''
        const response = await fetch(this.serverURL + `/${operatorName}${cantonSuffix}`)
        if (response.status === 200) {
            return await response.json();
        }
        throw `${this.serverURL}: Server responded with non-200 code!`
    }

    /**
     * Makes an API call to Flask server using the cantonName as a GET parameter and returns the data received or
     * throws an error if the server responds with anything other than status-code 200.
     * @param cantonName
     * @returns {Promise<Any[]>}
     */
    async fetchATMsByCanton(cantonName) {
        const response = await fetch(this.serverURL + `/canton/${cantonName}`)
        if (response.status === 200) {
            return await response.json();
        }
        throw `${this.serverURL}: Server responded with non-200 code!`
    }
}

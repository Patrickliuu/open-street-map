/**
 * Initiate Bar Chart.
 */
async function init() {
    const api = new APIHandler();
    const apiData = await api.fetchATMs();
    createATMChart(apiData, 'bar-chart')
}

init();


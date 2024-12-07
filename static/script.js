function predictPrice() {
    event.preventDefault();
    const brand = document.getElementById('brand').value;
    const RAM = document.getElementById('RAM').value;
    const InternalMemory = document.getElementById('InternalMemory').value;
    const DisplaySize = document.getElementById('DisplaySize').value;
    const material = document.getElementById('material').value;

    if (!brand || brand === "Select Brand" || !RAM || RAM === "Select RAM" || !InternalMemory || InternalMemory === "Select InternalMemory" || !DisplaySize || DisplaySize === "Select DisplaySize" || !Battery || material === "Select Material") {
        alert("Please select options for all fields.");
        return false;
    }
    document.getElementById('pricePredictionForm').submit();
    return true;
    
}
function predictPrice(event) {
    event.preventDefault();

    const Brand = document.getElementById('Brand').value;
    const RAM = document.getElementById('RAM').value;
    const InternalMemory = document.getElementById('InternalMemory').value; // Updated for consistency
    const DisplaySize = document.getElementById('DisplaySize').value; // Updated for consistency
    const Battery = document.getElementById('Battery').value;

    // Validation check for required fields
    if (!Brand || Brand === "Select Brand" || !RAM || RAM === "Enter RAM" || !DisplaySize || DisplaySize === "Enter DisplaySize" || !Battery || Battery === "Enter Battery" || !InternalMemory || InternalMemory === "Enter InternalMemory") {
        alert("Please select options for all fields.");
        return false;
    }

    // // Numeric validation for RAM, InternalMemory, Battery, and DisplaySize
    // if (isNaN(RAM) || isNaN(InternalMemory) || isNaN(Battery) || isNaN(DisplaySize)) {
    //     alert("Please enter valid numeric values for RAM, Internal Memory, Battery, and Display Size.");
    //     return false;
    // }

    // // Optional: Range validation (if needed)
    // if (RAM < 0 || InternalMemory < 0|| Battery < 0 || DisplaySize < 0) {
    //     alert("Please enter values greater than zero for RAM, Internal Memory, Battery, and Display Size.");
    //     return false;
    // }

    // If all fields are valid, submit the form
    document.getElementById('pricePredictionForm').submit();
    return true;
}


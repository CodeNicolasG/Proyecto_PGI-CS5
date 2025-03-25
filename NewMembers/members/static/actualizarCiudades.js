const ciudadesPorProvincia = {
    "Buenos Aires": ["La Plata", "Mar del Plata", "Bahía Blanca"],
    "CABA": ["Buenos Aires"],
    "Catamarca": ["San Fernando del Valle de Catamarca"],
    "Chaco": ["Resistencia", "Saenz Peña"],
    "Chubut": ["Rawson", "Comodoro Rivadavia"],
    "Córdoba": ["Córdoba", "Villa María", "Río Cuarto"],
    "Corrientes": ["Corrientes", "Goya"],
    "Entre Ríos": ["Paraná", "Concordia"],
    "Formosa": ["Formosa"],
    "Jujuy": ["San Salvador de Jujuy"],
    "La Pampa": ["Santa Rosa"],
    "La Rioja": ["La Rioja"],
    "Mendoza": ["Mendoza", "San Rafael"],
    "Misiones": ["Posadas", "Oberá"],
    "Neuquén": ["Neuquén"],
    "Río Negro": ["Viedma", "San Carlos de Bariloche"],
    "Salta": ["Salta"],
    "San Juan": ["San Juan"],
    "San Luis": ["San Luis"],
    "Santa Cruz": ["Río Gallegos"],
    "Santa Fe": ["Santa Fe", "Rosario"],
    "Santiago del Estero": ["Santiago del Estero"],
    "Tierra del Fuego": ["Ushuaia", "Río Grande"],
    "Tucumán": ["San Miguel de Tucumán"]
};

function actualizarCiudades() {
    const provinciaSeleccionada = document.getElementById("provincia").value;
    const ciudadSelect = document.getElementById("ciudad");

    ciudadSelect.innerHTML = '<option value="">Seleccione una ciudad</option>'; 

    if (ciudadesPorProvincia[provinciaSeleccionada]) {
        ciudadesPorProvincia[provinciaSeleccionada].forEach(ciudad => {
            let option = document.createElement("option");
            option.value = ciudad;
            option.textContent = ciudad;
            ciudadSelect.appendChild(option);
        });
    }
}

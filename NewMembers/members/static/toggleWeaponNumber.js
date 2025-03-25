// Función para manejar la activación/desactivación del campo de número de armamento
function toggleWeaponNumber() {
    var weaponAssigned = document.getElementById('weapon_assigned').value;
    var weaponNumber = document.getElementById('weapon_number');
    if (weaponAssigned === 'si') {
        weaponNumber.disabled = false;
    } else {
        weaponNumber.disabled = true;
        weaponNumber.value = '';  // Limpia el valor cuando se deshabilita
    }
}

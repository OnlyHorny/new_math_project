function showForm(materialType) {
    if (materialType === 'theory') {
        document.getElementById('theoryForm').style.display = 'block';
        document.getElementById('theoryMaterialForm').style.display = 'block';
        document.getElementById('practiceForm').style.display = 'none';
        document.getElementById('practiceMaterialForm').style.display = 'none';
    } else if (materialType === 'practice') {
        document.getElementById('theoryForm').style.display = 'none';
        document.getElementById('theoryMaterialForm').style.display = 'none';
        document.getElementById('practiceForm').style.display = 'block';
        document.getElementById('practiceMaterialForm').style.display = 'block';
    }
}

function submitForm(formId) {
    alert('Заявка успешно отправлена!');
}

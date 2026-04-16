async function alreadyLogin() {
    try {
        const response = await fetch('/api/v1/auth/' , {
            method: 'POST',
        });
        if (!response.ok) {
            return null;
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}

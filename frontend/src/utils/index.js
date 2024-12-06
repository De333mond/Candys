export function courtEqual(obj1, obj2) {
    return obj1.item === obj2.item &&
        obj1.additionalInfo.title === obj2.additionalInfo.title &&
        obj1.additionalInfo.fillingId === obj2.additionalInfo.fillingId
}


export function formatDate(date) {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    const hours = String(date.getHours()).padStart(2, '0');
    const minutes = String(date.getMinutes()).padStart(2, '0');

    const timezoneOffset = date.getTimezoneOffset();
    const timezoneOffsetSign = timezoneOffset > 0 ? '-' : '+';
    const timezoneOffsetHours = String(Math.floor(Math.abs(timezoneOffset) / 60)).padStart(2, '0');
    const timezoneOffsetMinutes = String(Math.abs(timezoneOffset) % 60).padStart(2, '0');

    const timezone = timezoneOffset === 0 ? 'Z' : timezoneOffsetSign + timezoneOffsetHours + ':' + timezoneOffsetMinutes;

    return `${year}-${month}-${day}T${hours}:${minutes}${timezone}`;
}


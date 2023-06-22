/* Javascript for CounterXBlock. */
function CounterXBlock(runtime, element) {
	function updateCount(result) {
		console.log(result);
		$('#counter-value', element).text(result.count);
	}

	const handlerUrlUpdateCount = runtime.handlerUrl(element, 'update_count');
	const handlerUrlResetCount = runtime.handlerUrl(element, 'reset_count');

	$('#increment-btn', element).click(function (eventObject) {
		$.ajax({
			type: 'POST',
			url: handlerUrlUpdateCount,
			data: JSON.stringify({ count: 1 }),
			success: updateCount,
		});
	});
	$('#decrement-btn', element).click(function (eventObject) {
		$.ajax({
			type: 'POST',
			url: handlerUrlUpdateCount,
			data: JSON.stringify({ count: -1 }),
			success: updateCount,
		});
	});

	$('#reset', element).click(function (eventObject) {
		$.ajax({
			type: 'POST',
			url: handlerUrlResetCount,
			data: JSON.stringify({ count: -1 }),
			success: updateCount,
		});
	});

	$(function ($) {
		/* Here's where you'd do things on page load. */
	});
}

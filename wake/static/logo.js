function Sphere(color, radius, x, y, z) {
    this.color = color;
    this.lineWidth = 1;
    this.radius = radius;
    this.x = x;
    this.y = y;
    this.z = z;
}
Sphere.prototype = {
    draw: function(ctx) {
        var scale = 200/(200 + this.z),
            size = this.radius * scale,
            shading = (1 + this.z/20); 
        ctx.save();
        ctx.translate(16 + this.x*scale, 16 + this.y*scale);
        ctx.beginPath();
        ctx.arc(0, 0, size, 0, 2*Math.PI, false);
        ctx.fillStyle = this.color;
        ctx.fill();
        ctx.strokeStyle = 'black';
        ctx.lineWidth = this.lineWidth;
        ctx.stroke();
        ctx.restore();
    }
}

$(document).ready(function() {
    spheres = [];
    
    var radius = 4,
        size = radius,
        sin60 = Math.sin(Math.PI/3);
    spheres.push(new Sphere("#fed00b", radius, 0, 0, 0));
    spheres.push(new Sphere("#feff00", radius, size, -size*2*sin60, 0));
    spheres.push(new Sphere("#feff00", radius, -size, -size*2*sin60, 0));
    spheres.push(new Sphere("#fe5e09", radius, -size*2, 0, 0));
    spheres.push(new Sphere("#fe5e09", radius, size*2, 0, 0));
    spheres.push(new Sphere("#fed00b", radius, -size, size*2*sin60, 0));
    spheres.push(new Sphere("#fed00b", radius, size, size*2*sin60, 0));
    $.each(spheres, function(index, sphere) {
        sphere.distance = sphere.x;
    });
    
    var r = 0,
        count = 0,
        logo = $('#logo'),
        canvas = $('#logo-canvas')[0],
        ctx = canvas.getContext('2d');

    canvas.width = canvas.height = "32"

    // TODO: requestFrame
    window.setInterval(function() {
        ctx.clearRect(0,0,32,32);
        var hovered = logo.hasClass('hover');
        $.each(spheres, function(index, sphere) {
            sphere.lineWidth = hovered ? 1.5 : 1.1;
            sphere.z = sphere.distance*Math.sin(r);
            sphere.x = sphere.distance*Math.cos(r);
        });
        spheres.sort(function(sphere1, sphere2) { return sphere2.z - sphere1.z; });
        $.each(spheres, function(index, sphere) {
            sphere.draw(ctx);
        });
        r = (r + .04 + Math.max(0, .12*(Math.sin(count)))) % (2*Math.PI);
        count = (count + .025) % (2*Math.PI);
        
        logo.hover(
            function () {
                $(this).addClass("hover");
            },
            function () {
                $(this).removeClass("hover");
            }
        );
    }, 60);
});

/* [Print Layout] */

// Preview the parts in the optimal orientation for 3D printing.
print_orientation = false; // [true, false]
// Additional spacing between key trays in print orientation to prevent brim collision.
print_tray_spacing_mm = 5; // [0:1:50]

// printer bed dimensions
printer = "p1s"; // [p1s, ender3v2]
bed_x_mm = printer == "p1s" ? 250 : 220;
bed_y_mm = printer == "p1s" ? 250 : 220;

/* [Key Profile] */

// Select the key spacing standard used to size each tray footprint.
key_profile = "choc"; // [mx, choc]

/* [3D Printing] */

// 3D printing settings and validation.
spiral_vase = true; // [true, false]
nozzle_width_mm = 0.4; // [0.2:0.05:1.0]

// Shared wall and floor dimensions.
wall_lines = 1; // [1:1:5]
floor_layers = 1; // [1:1:5]

// Effective print dimensions. Spiral vase mode forces single-line walls and floor.
effective_wall_thickness_mm = spiral_vase ? nozzle_width_mm : wall_lines * nozzle_width_mm;
effective_floor_thickness_mm = spiral_vase ? nozzle_width_mm : floor_layers * nozzle_width_mm;

assert(nozzle_width_mm > 0, "nozzle_width_mm must be greater than 0");
assert(wall_lines > 0, "wall_lines must be greater than 0");
assert(floor_layers > 0, "floor_layers must be greater than 0");
assert(default_clearance_mm >= 0, "default_clearance_mm must be non-negative");
assert(
  !spiral_vase || wall_lines == 1,
  "spiral_vase requires wall_lines to be exactly 1"
);
assert(
  !spiral_vase || floor_layers == 1,
  "spiral_vase requires floor_layers to be exactly 1"
);

/* [Clearance] */

// General fit clearance applied to most nested parts.
default_clearance_mm = 0.4; // [0:0.05:1.0]
// Fit clearance around the tray container inside the drawer.
drawer_clearance_mm = 0.3; // [0:0.05:1.0]
// Fit clearance around individual trays inside the container.
tray_container_clearance_mm = 0.3; // [0:0.05:1.0]

/* [Key Trays] */

// Layout sizing: trays span the full row width/depth, with one tray per row.
tray_orientation = "width"; // [width, length]
tray_count = [3, 2]; // [1:1:12]

// Tray-specific sizing controls.
max_keycap_height_mm = 17; // [8:0.5:30]
tray_lip_height_mm = 5; // [1:0.5:20]
tray_length_u = 1; // [1:1:8]

/* [Tray Container Handle] */

// Dimensions and angle of the handle slope on the tray container.
handle_height_mm = 10; // [0:0.5:20]
handle_width_mm = 3; // [0:0.5:20]
// Angle of the handle slope relative to plate, can easily break handle if too steep.
handle_angle_deg = 60; // [30:5:80]

/* [Advanced Geometry] */

// Tiny vertical corner rounding to smooth toolpaths without materially changing fit.
vertical_corner_radius_mm = 0.4; // [0:0.05:1.0]

/* [Key Tray Spacing] */

// Standard key spacing dimensions.
mx_key_spacing_mm = 19.05; // [18:0.05:20]
choc_key_spacing_x_mm = 18; // [16:0.05:20]
choc_key_spacing_y_mm = 17; // [16:0.05:20]

/* [Hidden] */

// Spread the drawer, container, and trays apart for inspection.
debug_exploded_view = false; // [true, false]
debug_explode_distance_mm = print_tray_spacing_mm; // [0:1:100]

fancy_render = true;
$fn = fancy_render ? 50 : 10;

// Resolve the active spacing from the selected key profile.
key_spacing_x_mm = key_profile == "mx" ? mx_key_spacing_mm : choc_key_spacing_x_mm;
key_spacing_y_mm = key_profile == "mx" ? mx_key_spacing_mm : choc_key_spacing_y_mm;

// A tray is fixed to 1u in y, while row width in x and lip height in z remain parametric.
row_tray_width_u = tray_orientation == "width" ? tray_count[0] : tray_length_u;
row_tray_length_u = tray_orientation == "width" ? tray_length_u : tray_count[0];
tray_height_mm = tray_lip_height_mm;
stack_height_mm = max_keycap_height_mm + default_clearance_mm * 2;

// Inner tray envelope sized around one row-wide tray footprint plus fit clearance.
tray_inner_x_mm = key_spacing_x_mm * row_tray_width_u + default_clearance_mm * 2;
tray_inner_y_mm = key_spacing_y_mm * row_tray_length_u + default_clearance_mm * 2;
tray_inner_z_mm = tray_height_mm;

// Outer tray shell dimensions.
tray_outer_x_mm = tray_inner_x_mm + effective_wall_thickness_mm * 2;
tray_outer_y_mm = tray_inner_y_mm + effective_wall_thickness_mm * 2;
tray_outer_z_mm = tray_inner_z_mm + effective_floor_thickness_mm;
tray_outer_corner_radius_mm = min(vertical_corner_radius_mm, min(tray_outer_x_mm, tray_outer_y_mm) / 2);
tray_inner_corner_radius_mm = max(0, tray_outer_corner_radius_mm - effective_wall_thickness_mm);

// Container inner cavity sized to receive one tray per row and the full key stack height.
tray_container_inner_x_mm =
  tray_orientation == "width" ?
    tray_outer_x_mm + tray_container_clearance_mm * 2
  : tray_outer_x_mm * tray_count[0] + tray_container_clearance_mm * 2;
tray_container_inner_y_mm =
  tray_orientation == "width" ?
    tray_outer_y_mm * tray_count[1] + tray_container_clearance_mm * 2
  : tray_outer_y_mm + tray_container_clearance_mm * 2;
tray_container_inner_z_mm = stack_height_mm + effective_floor_thickness_mm + tray_container_clearance_mm;

// Outer container shell dimensions.
tray_container_outer_x_mm = tray_container_inner_x_mm + effective_wall_thickness_mm * 2;
tray_container_outer_y_mm = tray_container_inner_y_mm + effective_wall_thickness_mm * 2;
tray_container_outer_z_mm = tray_container_inner_z_mm + effective_floor_thickness_mm;
tray_container_outer_corner_radius_mm = min(vertical_corner_radius_mm, min(tray_container_outer_x_mm, tray_container_outer_y_mm) / 2);
tray_container_inner_corner_radius_mm = max(0, tray_container_outer_corner_radius_mm - effective_wall_thickness_mm);
handle_rise_mm = min(10, tray_container_outer_z_mm);
handle_run_mm = handle_rise_mm / tan(handle_angle_deg);
handle_projection_mm = max(handle_height_mm, handle_run_mm);
handle_corner_radius_mm = min(2, handle_rise_mm / 2, handle_projection_mm / 2);
handle_fillet_adjacent_mm = handle_corner_radius_mm / tan(handle_angle_deg);
handle_hypotenuse_mm = handle_rise_mm / sin(handle_angle_deg);

// Drawer inner cavity sized to receive the tray container from the front.
drawer_inner_x_mm = tray_container_outer_x_mm + drawer_clearance_mm * 2;
drawer_inner_y_mm = tray_container_outer_y_mm + drawer_clearance_mm + effective_wall_thickness_mm;
drawer_inner_z_mm = tray_container_outer_z_mm + drawer_clearance_mm;

// Outer drawer shell dimensions.
drawer_outer_x_mm = drawer_inner_x_mm + effective_wall_thickness_mm * 2;
drawer_outer_y_mm = drawer_inner_y_mm + effective_wall_thickness_mm;
drawer_outer_z_mm = drawer_inner_z_mm + effective_floor_thickness_mm + effective_wall_thickness_mm;
drawer_outer_corner_radius_mm = min(vertical_corner_radius_mm, min(drawer_outer_x_mm, drawer_outer_y_mm) / 2);
drawer_inner_corner_radius_mm = max(0, drawer_outer_corner_radius_mm - effective_wall_thickness_mm);

// Build a rounded rectangular prism with tiny fillets on the vertical corners.
module rounded_rect_prism(size, radius) {
  linear_extrude(height=size[2])
    offset(r=radius)
      translate([radius, radius])
        square(
          [
            max(0.01, size[0] - radius * 2),
            max(0.01, size[1] - radius * 2),
          ]
        );
}

module tray_container_handle_body(
  handle_width_mm = handle_width_mm,
  effective_floor_thickness_mm = effective_floor_thickness_mm,
  thickness_offset_mm = 0,
  y_extension_mm = 0
) {
  // We want to pull the front face inward by thickness_offset_mm to leave wall thickness.
  local_rise = max(0.01, handle_rise_mm - effective_floor_thickness_mm);
  local_run = local_rise / tan(handle_angle_deg);
  // Ensure local_projection is at least local_run to prevent self-intersecting polygon
  local_projection = max(local_run, handle_projection_mm / 2 - thickness_offset_mm);

  // Rotate[90, 180, 270] mapping logic:
  // 1. Z-axis extrusion maps to World X (left-to-right). This means the handle spans
  //    across the tray from `(tray_container_outer_x_mm + handle_width_mm) / 2` 
  //    towards the left by `handle_width_mm`.
  // 2. Local X-axis maps to World -Y (outward projection). Negative local X values 
  //    project forward away from the tray.
  // 3. Local Y-axis maps to World -Z (downward depth). Negative local Y values
  //    extend upwards from the floor.
  // The translation ensures the base of the sloped face aligns perfectly with the tray wall.
  translate(
    [
      (tray_container_outer_x_mm + handle_width_mm) / 2,
      local_projection - local_run + effective_wall_thickness_mm, // align bottom of slope with tray face
      effective_floor_thickness_mm, // Bottom at floor level
    ]
  )
    rotate([90, 180, 270])
      linear_extrude(height=handle_width_mm)
        polygon(
          points=[
            [y_extension_mm, 0], // Back Bottom (at floor level)
            [-local_projection + local_run, 0], // Front Bottom
            [-local_projection, -local_rise], // Front Top (max height)
            [y_extension_mm, -local_rise], // Back Top
          ]
        );
}

module tray_container_handle_side_fillet_cutter(
  side,
  handle_corner_radius_mm = handle_corner_radius_mm,
  handle_width_mm = handle_width_mm,
  effective_floor_thickness_mm = effective_floor_thickness_mm
) {
  if (side < 0) {
    difference() {
      translate(
        [
          (tray_container_outer_x_mm - handle_width_mm) / 2 - handle_corner_radius_mm,
          -handle_corner_radius_mm,
          effective_floor_thickness_mm,
        ]
      )
        cube(
          [
            handle_corner_radius_mm,
            handle_corner_radius_mm,
            handle_rise_mm,
          ]
        );
      translate(
        [
          (tray_container_outer_x_mm - handle_width_mm) / 2 - handle_corner_radius_mm,
          -handle_corner_radius_mm,
          effective_floor_thickness_mm,
        ]
      )
        cylinder(h=handle_rise_mm, r=handle_corner_radius_mm);
    }
  } else {
    translate(
      [
        (tray_container_outer_x_mm + handle_width_mm) / 2 + handle_corner_radius_mm,
        -handle_corner_radius_mm,
        effective_floor_thickness_mm,
      ]
    )
      rotate([0, 0, 270])
        translate(
          [
            -(tray_container_outer_x_mm + handle_width_mm) / 2,
            handle_corner_radius_mm,
            -effective_floor_thickness_mm,
          ]
        )
          difference() {
            translate(
              [
                (tray_container_outer_x_mm + handle_width_mm) / 2,
                -handle_corner_radius_mm,
                effective_floor_thickness_mm,
              ]
            )
              cube(
                [
                  handle_corner_radius_mm,
                  handle_corner_radius_mm,
                  handle_rise_mm,
                ]
              );
            translate(
              [
                (tray_container_outer_x_mm + handle_width_mm) / 2,
                -handle_corner_radius_mm,
                effective_floor_thickness_mm,
              ]
            )
              cylinder(h=handle_rise_mm, r=handle_corner_radius_mm);
          }
  }
}

module tray_container_handle_hypotenuse_fillet_cutter(
  side,
  handle_corner_radius_mm = handle_corner_radius_mm,
  handle_width_mm = handle_width_mm,
  effective_floor_thickness_mm = effective_floor_thickness_mm,
  handle_hypotenuse_mm = handle_hypotenuse_mm
) {
  angle = 90 - handle_angle_deg;
  if (side < 0) {
    translate(
      [
        (tray_container_outer_x_mm - handle_width_mm) / 2 - handle_corner_radius_mm,
        -handle_corner_radius_mm * 2 * tan(angle),
        effective_floor_thickness_mm,
      ]
    )
      rotate([-angle, 0, 180])
        translate(
          [
            -( (tray_container_outer_x_mm - handle_width_mm) / 2 + handle_corner_radius_mm),
            -handle_corner_radius_mm,
            -effective_floor_thickness_mm - (handle_corner_radius_mm * tan(angle)),
          ]
        )
          difference() {
            translate(
              [
                (tray_container_outer_x_mm - handle_width_mm) / 2 - handle_corner_radius_mm,
                -handle_corner_radius_mm,
                effective_floor_thickness_mm,
              ]
            )
              cube(
                [
                  handle_corner_radius_mm,
                  handle_corner_radius_mm,
                  handle_hypotenuse_mm,
                ]
              );
            translate(
              [
                (tray_container_outer_x_mm - handle_width_mm) / 2 - handle_corner_radius_mm,
                -handle_corner_radius_mm,
                effective_floor_thickness_mm,
              ]
            )
              cylinder(h=handle_hypotenuse_mm, r=handle_corner_radius_mm);
          }
  } else {
    translate([tray_container_outer_x_mm, 0, 0])
      mirror([1, 0, 0])
        tray_container_handle_hypotenuse_fillet_cutter(
          -1,
          handle_corner_radius_mm=handle_corner_radius_mm,
          handle_width_mm=handle_width_mm,
          effective_floor_thickness_mm=effective_floor_thickness_mm,
          handle_hypotenuse_mm=handle_hypotenuse_mm
        );
  }
}

// Build the front tray-container handle as an angled prism rising from the base.
module tray_container_handle(
  handle_corner_radius_mm = handle_corner_radius_mm,
  handle_width_mm = handle_width_mm,
  effective_floor_thickness_mm = effective_floor_thickness_mm,
  handle_hypotenuse_mm = handle_hypotenuse_mm,
  thickness_offset_mm = 0,
  y_extension_mm = 0
) {
  // TODO: add fillets to the handle
  difference() {
    union() {
      tray_container_handle_body(
        handle_width_mm=handle_width_mm,
        effective_floor_thickness_mm=effective_floor_thickness_mm,
        thickness_offset_mm=thickness_offset_mm,
        y_extension_mm=y_extension_mm
      );
      // tray_container_handle_side_fillet_cutter(
      //   -1,
      //   handle_corner_radius_mm=handle_corner_radius_mm,
      //   handle_width_mm=handle_width_mm,
      //   effective_floor_thickness_mm=effective_floor_thickness_mm
      // );
      // tray_container_handle_side_fillet_cutter(
      //   1,
      //   handle_corner_radius_mm=handle_corner_radius_mm,
      //   handle_width_mm=handle_width_mm,
      //   effective_floor_thickness_mm=effective_floor_thickness_mm
      // );
    }
    ;
    // tray_container_handle_hypotenuse_fillet_cutter(
    //   -1,
    //   handle_corner_radius_mm=handle_corner_radius_mm,
    //   handle_width_mm=handle_width_mm,
    //   effective_floor_thickness_mm=effective_floor_thickness_mm,
    //   handle_hypotenuse_mm=handle_hypotenuse_mm
    // );
    // tray_container_handle_hypotenuse_fillet_cutter(
    //   1,
    //   handle_corner_radius_mm=handle_corner_radius_mm,
    //   handle_width_mm=handle_width_mm,
    //   effective_floor_thickness_mm=effective_floor_thickness_mm,
    //   handle_hypotenuse_mm=handle_hypotenuse_mm
    // );
  }
}

// Take the handle and subtract a smaller handle
module tray_container_handle_with_cutout(
  handle_corner_radius_mm = handle_corner_radius_mm,
  handle_width_mm = handle_width_mm,
  effective_floor_thickness_mm = effective_floor_thickness_mm,
  handle_hypotenuse_mm = handle_hypotenuse_mm
) {
  difference() {
    tray_container_handle(
      handle_corner_radius_mm=handle_corner_radius_mm,
      handle_width_mm=handle_width_mm,
      effective_floor_thickness_mm=effective_floor_thickness_mm,
      handle_hypotenuse_mm=handle_hypotenuse_mm
    );
    tray_container_handle(
      handle_corner_radius_mm=handle_corner_radius_mm - effective_wall_thickness_mm,
      handle_width_mm=handle_width_mm - effective_wall_thickness_mm * 2,
      effective_floor_thickness_mm=effective_floor_thickness_mm + effective_wall_thickness_mm,
      handle_hypotenuse_mm=handle_hypotenuse_mm
    );
  }
}

// Build a single open-top tray.
module key_tray() {
  difference() {
    rounded_rect_prism(
      [tray_outer_x_mm, tray_outer_y_mm, tray_outer_z_mm],
      tray_outer_corner_radius_mm
    );
    translate([effective_wall_thickness_mm, effective_wall_thickness_mm, effective_floor_thickness_mm])
      rounded_rect_prism(
        [tray_inner_x_mm, tray_inner_y_mm, tray_inner_z_mm],
        tray_inner_corner_radius_mm
      );
  }
}

// Build the open-top container shell that holds one or more trays.
module tray_container() {
  difference() {
    union() {
      difference() {
        rounded_rect_prism(
          [tray_container_outer_x_mm, tray_container_outer_y_mm, tray_container_outer_z_mm],
          tray_container_outer_corner_radius_mm
        );
        translate([effective_wall_thickness_mm, effective_wall_thickness_mm, effective_floor_thickness_mm])
          rounded_rect_prism(
            [tray_container_inner_x_mm, tray_container_inner_y_mm, tray_container_inner_z_mm],
            tray_container_inner_corner_radius_mm
          );
      }
      ;
      // TODO: add fillets to the handle
      tray_container_handle(
        handle_corner_radius_mm=handle_corner_radius_mm,
        handle_width_mm=handle_width_mm,
        effective_floor_thickness_mm=effective_floor_thickness_mm,
        handle_hypotenuse_mm=handle_hypotenuse_mm
      );
    }

    tray_container_handle(
      handle_corner_radius_mm=handle_corner_radius_mm - effective_wall_thickness_mm,
      handle_width_mm=handle_width_mm - effective_wall_thickness_mm * 2,
      effective_floor_thickness_mm=effective_floor_thickness_mm + effective_wall_thickness_mm,
      handle_hypotenuse_mm=handle_hypotenuse_mm,
      thickness_offset_mm=effective_wall_thickness_mm,
      y_extension_mm=effective_wall_thickness_mm * 2
    );
  }
}

// Build the outer drawer shell with a front opening for the tray container.
module outer_drawer() {
  difference() {
    rounded_rect_prism(
      [drawer_outer_x_mm, drawer_outer_y_mm, drawer_outer_z_mm],
      drawer_outer_corner_radius_mm
    );
    translate([effective_wall_thickness_mm, 0, effective_floor_thickness_mm])
      rounded_rect_prism(
        [drawer_inner_x_mm, drawer_inner_y_mm, drawer_inner_z_mm],
        drawer_inner_corner_radius_mm
      );
  }
}

// Place one tray in each row so the tray width follows the container width.
module tray_container_layout() {
  if (tray_orientation == "width") {
    for (iy = [0:tray_count[1] - 1]) {
      translate(
        [
          effective_wall_thickness_mm + tray_container_clearance_mm,
          effective_wall_thickness_mm + tray_container_clearance_mm + iy * tray_outer_y_mm,
          effective_floor_thickness_mm,
        ]
      )
        key_tray();
    }
  } else {
    for (ix = [0:tray_count[0] - 1]) {
      translate(
        [
          effective_wall_thickness_mm + tray_container_clearance_mm + ix * tray_outer_x_mm,
          effective_wall_thickness_mm + tray_container_clearance_mm,
          effective_floor_thickness_mm,
        ]
      )
        key_tray();
    }
  }
}

// Preview the fitted relationship between the tray container and its trays.
module tray_container_assembly() {
  tray_container();
  tray_container_layout();
}

// Preview the drawer, container, and trays separated for easier inspection.
module exploded_drawer_assembly() {
  outer_drawer();
  translate(
    [
      drawer_outer_x_mm + debug_explode_distance_mm,
      0,
      0,
    ]
  )
    tray_container();
  translate(
    [
      drawer_outer_x_mm + tray_container_outer_x_mm + debug_explode_distance_mm * 2,
      0,
      0,
    ]
  )
    tray_container_layout();
}

// Preview the fitted relationship between the drawer, container, and trays.
module drawer_assembly() {
  outer_drawer();
  translate(
    [
      effective_wall_thickness_mm + drawer_clearance_mm,
      0,
      effective_floor_thickness_mm,
    ]
  )
    tray_container_assembly();
}

module print_drawer_assembly() {
  translate([0, 0, drawer_outer_y_mm])
    rotate([-90, 0, 0])
      outer_drawer();

  translate(
    [
      drawer_outer_x_mm + debug_explode_distance_mm,
      0,
      0,
    ]
  )
    tray_container();

  translate(
    [
      drawer_outer_x_mm + tray_container_outer_x_mm + debug_explode_distance_mm * 2,
      0,
      0,
    ]
  ) if (tray_orientation == "width") {
    for (iy = [0:tray_count[1] - 1]) {
      translate([0, iy * (tray_outer_y_mm + print_tray_spacing_mm), 0])
        key_tray();
    }
  } else {
    for (ix = [0:tray_count[0] - 1]) {
      translate([ix * (tray_outer_x_mm + print_tray_spacing_mm), 0, 0])
        key_tray();
    }
  }
}

if (print_orientation) {
  print_drawer_assembly();
} else if (debug_exploded_view) {
  exploded_drawer_assembly();
} else {
  drawer_assembly();
}

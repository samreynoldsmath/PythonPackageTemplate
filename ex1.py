import mypackage as pkg

pkg.mod_u.hello()
pkg.mod_v.hello()

pkg.src1.mod_a.hello()
pkg.src1.mod_b.hello()

pkg.src2.mod_x.hello()
pkg.src2.mod_y.hello()

pkg.src1.src_A.mod_p.hello()
pkg.src1.src_A.mod_q.hello()

pkg.src1.mod_c.hello_from_other_subpackage()

pkg.thing.thing.thing('howdy pardner')
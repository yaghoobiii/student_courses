/*
 * student-courses
 * The API for the Maryam's homework
 *
 * OpenAPI spec version: 2.0.0
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 3.0.42
 *
 * Do not edit the class manually.
 *
 */
(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', '../../src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require('../../src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.StudentCourses);
  }
}(this, function(expect, StudentCourses) {
  'use strict';

  var instance;

  describe('(package)', function() {
    describe('Course', function() {
      beforeEach(function() {
        instance = new StudentCourses.Course();
      });

      it('should create an instance of Course', function() {
        // TODO: update the code to test Course
        expect(instance).to.be.a(StudentCourses.Course);
      });

      it('should have the property id (base name: "id")', function() {
        // TODO: update the code to test the property id
        expect(instance).to.have.property('id');
        // expect(instance.id).to.be(expectedValueLiteral);
      });

      it('should have the property name (base name: "name")', function() {
        // TODO: update the code to test the property name
        expect(instance).to.have.property('name');
        // expect(instance.name).to.be(expectedValueLiteral);
      });

      it('should have the property teacherName (base name: "teacher_name")', function() {
        // TODO: update the code to test the property teacherName
        expect(instance).to.have.property('teacherName');
        // expect(instance.teacherName).to.be(expectedValueLiteral);
      });

      it('should have the property weakDay (base name: "weak_day")', function() {
        // TODO: update the code to test the property weakDay
        expect(instance).to.have.property('weakDay');
        // expect(instance.weakDay).to.be(expectedValueLiteral);
      });

      it('should have the property startTime (base name: "start_time")', function() {
        // TODO: update the code to test the property startTime
        expect(instance).to.have.property('startTime');
        // expect(instance.startTime).to.be(expectedValueLiteral);
      });

      it('should have the property endTime (base name: "end_time")', function() {
        // TODO: update the code to test the property endTime
        expect(instance).to.have.property('endTime');
        // expect(instance.endTime).to.be(expectedValueLiteral);
      });

    });
  });

}));

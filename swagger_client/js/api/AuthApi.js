/*
 * student-courses
 * The API for the Maryam's homework
 *
 * OpenAPI spec version: 2.1.0
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 3.0.42
 *
 * Do not edit the class manually.
 *
 */
import {ApiClient} from "../ApiClient";
import {LoginStatus} from '../model/LoginStatus';

/**
* Auth service.
* @module api/AuthApi
* @version 2.1.0
*/
export class AuthApi {

    /**
    * Constructs a new AuthApi. 
    * @alias module:api/AuthApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instanc
    e} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }

    /**
     * Callback function to receive the result of the login operation.
     * @callback moduleapi/AuthApi~loginCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LoginStatus{ data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Login interface for students
     * @param {String} userId 
     * @param {String} password 
     * @param {module:api/AuthApi~loginCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link <&vendorExtensions.x-jsdoc-type>}
     */
    login(userId, password, callback) {
      
      let postBody = null;
      // verify the required parameter 'userId' is set
      if (userId === undefined || userId === null) {
        throw new Error("Missing the required parameter 'userId' when calling login");
      }
      // verify the required parameter 'password' is set
      if (password === undefined || password === null) {
        throw new Error("Missing the required parameter 'password' when calling login");
      }

      let pathParams = {
        
      };
      let queryParams = {
        'user_id': userId,'password': password
      };
      let headerParams = {
        
      };
      let formParams = {
        
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = LoginStatus;

      return this.apiClient.callApi(
        '/login', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

}
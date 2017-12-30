import React, { Component } from "react";
import { Provider } from "react-redux";
import { createStore, applyMiddleware } from "redux";
import reducers from "./reducers";
import ReduxThunk from "redux-thunk";
import {
  TabNavigator,
  StackNavigator,
  DrawerNavigator
} from "react-navigation";

const store = createStore(reducers, {}, applyMiddleware(ReduxThunk));

const MainNavigator = StackNavigator({});

class Router extends Component {
  render() {
    return (
      <Provider store={store}>
        <MainNavigator />
      </Provider>
    );
  }
}

export default Router;

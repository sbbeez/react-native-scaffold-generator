const INITIAL_STATE = {};

export default (state = INITIAL_STATE, action) => {
  switch (action.type) {
    case ACTION_TYPE:
      return { ...state, action_var: action.payload };
    default:
      return state;
  }
};
